import cv2
import dlib
from scipy.spatial import distance as dist
import numpy as np
import pygame
from twilio.rest import Client
import sqlite3

# Load face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/home/cstup/Downloads/project2020-24/shape_predictor_68_face_landmarks.dat/shape_predictor_68_face_landmarks.dat")

pygame.init()
drum = pygame.mixer.Sound("/home/cstup/Downloads/wakeup and stay active sir.wav")
welcome=pygame.mixer.Sound("/home/cstup/Downloads/welcome.wav")
finish=pygame.mixer.Sound("/home/cstup/Downloads/sucked-into-classroom-103774.wav")
welcome.play()

# Function to calculate eye aspect ratio (EAR)
def eye_aspect_ratio(eye):
    # Compute the euclidean distances between the two sets of vertical eye landmarks
    A = dist.euclidean(eye[1], eye[5])  # 41, 47
    B = dist.euclidean(eye[2], eye[4])  # 42, 46

    # Compute the euclidean distance between the horizontal eye landmarks
    C = dist.euclidean(eye[0], eye[3])  # 40, 43

    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)
    return ear

  # Function to calculate mouth aspect ratio (MAR)
def mouth_aspect_ratio(mouth):
    # Compute the euclidean distances between the two sets of vertical mouth landmarks
    A = np.linalg.norm(mouth[3] - mouth[9])  # 51, 59
    B = np.linalg.norm(mouth[2] - mouth[10])  # 50, 58
    C = np.linalg.norm(mouth[4] - mouth[8])  # 52, 60

    # Compute the euclidean distance between the horizontal landmarks
    D = np.linalg.norm(mouth[0] - mouth[6])  # 48, 54

    # Compute the mouth aspect ratio
    mar = (A + B + C) / (3.0 * D)
    return mar

# Start video capture
cap = cv2.VideoCapture(0)

# Set thresholds for drowsiness and yawning detection
EAR_THRESHOLD = 0.25  # Eye aspect ratio threshold for drowsiness
MAR_THRESHOLD = 0.6   # Mouth aspect ratio threshold for yawning
CONSEC_FRAMES_DROWSY = 20  # Number of consecutive frames for drowsiness detection
CONSEC_FRAMES_YAWN = 15    # Number of consecutive frames for yawning detection

# Variables for counting consecutive frames with drowsiness and yawning
frame_count = 0
drowsy_frames = 0
yawn_frames = 0

##########################opening database test.db####################################################
#connect to the sqlite3 database
conn = sqlite3.connect('test.db')
print ("Opened database successfully for retrieve data");
#execute the sql query to select only the first row
cursor = conn.execute("SELECT account_sid, auth_token, twilio_phone_number, recipient_phone_number  from COMPANY LIMIT 1")

#fetch the first row
row = cursor.fetchone()

#print the data from the first row
if row:
#    Id=row[0]
   account_sid = row[0]
   auth_token = row[1]
   twilio_phone_number = row[2]
   recipient_phone_number= row[3]
   print(row[0])
   print(row[1])
   print(row[2])
   print(row[3])
   print('\n')
else:
    print("NO data found") 

#close the database connection
conn.close()



#####################################################################################################
while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale for Dlib processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = detector(gray)

    for face in faces:
        # Get coordinates of the bounding box for the detected face
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        
        # Draw a box around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Detect facial landmarks
        landmarks = predictor(gray, face)

        # Draw facial landmarks on the frame
        for n in range(0, 68):
            x_lm = landmarks.part(n).x
            y_lm = landmarks.part(n).y
            cv2.circle(frame, (x_lm, y_lm), 1, (0, 0, 255), -1)

        # Extract left and right eye landmarks
        left_eye = [(landmarks.part(n).x, landmarks.part(n).y) for n in range(36, 42)]
        right_eye = [(landmarks.part(n).x, landmarks.part(n).y) for n in range(42, 48)]

        # Calculate eye aspect ratios
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)

        # Compute average EAR
        ear = (left_ear + right_ear) / 2.0

        # Display Eye aspect ratio on the frame
        cv2.putText(frame, f'EAR: {ear:.2f}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Extract mouth landmarks
        mouth_points = np.array([[landmarks.part(n).x, landmarks.part(n).y] for n in range(48, 68)])

        # Calculate mouth aspect ratio
        mar = mouth_aspect_ratio(mouth_points)

        # Display Mouth aspect ratio on the frame
        cv2.putText(frame, f'MAR: {mar:.2f}', (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Check for yawning
        if mar > MAR_THRESHOLD:
            yawn_frames += 1
            if yawn_frames >= CONSEC_FRAMES_YAWN:
                cv2.putText(frame, "Yawning Detected", (50, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                #drum.play()

        else:
            yawn_frames = 0

        # Check for drowsiness
        if ear < EAR_THRESHOLD:
            drowsy_frames += 1
            if drowsy_frames >= CONSEC_FRAMES_DROWSY:
                cv2.putText(frame, "Drowsiness Detected", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                #drum.play()
   
        else:
            drowsy_frames = 0
        
        if(drowsy_frames==20):
            drum.play()
            #account_sid = '2b'
            #auth_token = 'a5d4'

            client = Client(account_sid, auth_token)
            message = client.messages.create( 
							from_=twilio_phone_number, 
							body ='Drowsiness detected(Location:26.864865,80.932897)', 
							to =recipient_phone_number) 

            print(message.sid)

        # Draw circles on the frame for visualization
        for (x, y) in left_eye + right_eye:
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

    # Display the resulting frame
    cv2.imshow('Driver Drowsiness and Yawn Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        finish.play()
        break

# Release the video capture
cap.release()
cv2.destroyAllWindows()

























































































