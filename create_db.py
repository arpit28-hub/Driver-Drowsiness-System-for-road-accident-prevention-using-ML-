import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");
conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY (
                    id INTEGER PRIMARY KEY,
                    account_sid TEXT,
                    auth_token TEXT,
                    twilio_phone_number TEXT,
                    recipient_phone_number TEXT
                  )''')

print("Table created successfully");

conn.close()