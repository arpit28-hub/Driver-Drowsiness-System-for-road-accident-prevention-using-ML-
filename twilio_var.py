
from twilio.rest import Client
import sqlite3
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



# Your Twilio Account SID, Authentication Token, and Twilio phone number
# account_sid = 'your_account_sid'
# auth_token = 'your_auth_token'
# twilio_phone_number = 'your_twilio_phone_number'

# Recipient's phone number
# recipient_phone_number = '+1234567890'


# Your message
# message_body = 'Hello from Twilio!'

# # Initialize Twilio client
# client = Client(account_sid, auth_token)

# try:
#     # Send SMS
#     message = client.messages.create(
#         body=message_body,
#         from_=twilio_phone_number,
#         to=recipient_phone_number
#     )
#     print("SMS sent successfully! SID:", message.sid)
# except Exception as e:
#     print("Error:", e)
