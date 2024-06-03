OPTIMAL SOLUTION FOR DRIVER DRWSINESS DETECTION USING MACHINE LEARNING



Overview

This project aims to develop a Driver Drowsiness Detection System using machine learning algorithms implemented via a Raspberry Pi. The system monitors the driver's eye movements and facial expressions to detect signs of drowsiness and alert the driver to take necessary action to prevent accidents.

Features

	Real-time monitoring of the driver's eyes and facial expressions.
	Detection of drowsiness using machine learning algorithms.
	Alerts the driver through audio or visual signals.
	Easy to set up and use with a Raspberry Pi.

Hardware Requirements

	Raspberry Pi (Model 3B+ or later recommended)
	USB webcam
	Speakers for alerting
	SD card with Raspberry Pi OS installed
	Power supply for Raspberry Pi

Software Requirements

	Python 3
	dlib library
	OpenCV library
	imutils library
	scipy library
	pygame library
	twilio library
	sqlite3 library
	Tkinter

Installation

Setting Up Raspberry Pi

1. Install Raspberry Pi OS 64 bit: Download and install the latest Raspberry Pi OS on an SD card.
2. Connect Hardware: Connect the power source (i.e.  Adapter 3-5V) to the raspberry Pi. Connect USB webcam (for video capturing) and Speakers (for alerting) to the Raspberry Pi.

Installing Necessary Libraries

1. Update and Upgrade Packages:
    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    ```
2. Install Python and pip:
    ```bash
    sudo apt-get install python3
    sudo apt-get install python3-pip
    ```
3. Install dlib:
    ```bash
    sudo apt-get install cmake
    pip3 install dlib
    ```
4. Install OpenCV:
    ```bash
    sudo apt-get install python3-opencv
    ```
5. Install imutils:
    ```bash
    pip3 install imutils 
    ```
6. Install scipy
 
```bash
    pip3 install scipy
    ```

 7.Install Twilio
```bash
    pip3 install Twilio 
    ```
8.Install pygame
```bash
    pip3 install pygame 
    ```
9. Install Tkinter
```bash
    pip3 install Tkinter 
    ```
10. Install sqlite3
```bash
    pip3 install sqlite3¬¬
    ```
Usage

Running the Detection Script

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd driver-drowsiness-detection
    ```
2. Download the pretrained facial landmark model for dlib:
    ```bash
    wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
    bunzip2 shape_predictor_68_face_landmarks.dat.bz2
    ```
3. Run the detection script:
    ```bash
    final_cstup_code19.py
    ```

Script Explanation

	final_cstup_code19.py: The main script that captures video from the camera, processes each frame to detect facial landmarks, and determines if the driver is drowsy based on eye aspect ratio (EAR).
	Main_gui.py: The script that enables user to interact with thee software via graphical user interface It enables user to change the twilio credentials.
	Create_db.py: The execution of this script create a database.
	Test: It is database file to store the user credentials.
	Geocoding.py: This script enables to get the current GPS location it the form of longitude and latitude coordinates.

Key Components

	Facial Landmark Detection: Using dlib's `shape_predictor_68_face_landmarks.dat` model to detect facial landmarks.
	Eye Aspect Ratio (EAR): Calculating EAR to determine eye closure. If the EAR is below a certain threshold for a predefined number of frames, the driver is considered drowsy.
	Mouth Aspect Ratio(MAR): Calculating MAR to determine yawning. If the MAR is below certain threshold, then driver is considered drowsy.
	Alert System: Triggering an alert using a speaker and send an SMS along with location if drowsiness is detected.

Customization

Modify the following parameters in `final_cstup_code19.py` to suit your needs:

	`EAR_THRESHOLD `: The EAR threshold below which the eyes are considered closed.

	`MAR_THRESHOLD`: The MAR threshold below which mouth is considered Yawning.

	`CONSEC_FRAMES_DROWSY`: The number of consecutive frames the EAR must be below the threshold to trigger an alert.

	`CONSEC_FRAMES_YAWN`: The number of consecutive frames the MAR must be below the threshold to trigger an alert. 


	Changing Alert Method: Modify the alert function in `final_cstup_code19.py` to change how the driver is alerted (e.g., using a different sound or alerting through some other means).

Troubleshooting

Common Issues

	Camera Not Detected: Ensure the camera is properly connected and enabled in the Raspberry Pi configuration settings.

	dlib Installation Errors: Ensure all dependencies are installed and you have enough memory to compile dlib.

	Tips
•	Test the system in various lighting conditions to ensure reliability.
•	Regularly update the Raspberry Pi OS and libraries to the latest versions.


Contributing

Feel free to contribute to this project by opening issues or submitting pull requests on the       repository.

Acknowledgments
 
	[dlib](http://dlib.net/)
	[OpenCV](https://opencv.org/)

---

For more detailed documentation and advanced configuration, please refer to the project's GitHub repository.
