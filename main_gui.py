# To configure the font of the title page to 'Comic Sans MS', you can add the `font` option to the style configuration for the title label. Here's how you can modify your code to achieve this:

# ```python
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Image and ImageTk modules from PIL

# PEVIOUS TEMP.PY

import sqlite3

class TwoPageGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Two Page GUI")

        # Create the pages
        self.title_page = TitlePage(self)
        self.page1 = LoginPage(self)
        self.page2 = Page2(self)

        # Show the title page by default
        self.title_page.pack(fill="both", expand=True)

        # Initialize the button to switch to page 2, but hide it
        self.switch_button = ttk.Button(self, text="Switch to Page 2", command=self.switch_page, style="Blue.TButton")
        self.switch_button.pack_forget()

        # Configure styles
        self.style = ttk.Style()
        self.style.configure("Title.TLabel", background="lightblue", font=("Comic Sans MS", 40, "bold"))
        self.style.configure("Blue.TButton", background="blue", foreground="black")

    def switch_page(self):
        """Switch between Page 1 and Page 2"""
        if self.switch_button.cget("text") == "Switch to Page 2":
            self.page1.pack_forget()
            self.page2.pack(fill="both", expand=True)
            self.switch_button.config(text="Switch to Page 1")
        else:
            self.page2.pack_forget()
            self.page1.pack(fill="both", expand=True)
            self.switch_button.config(text="Switch to Page 2")
            ####################################################title page##########################################################

class TitlePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(width=1000, height=700, background="blue")

        # Load and resize the background image
        image = Image.open("bcg.jpg")
        image = image.resize((1000, 700))
        self.background_image = ImageTk.PhotoImage(image)

        # Display the background image using a label
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create a frame to enclose the text
        text_frame = tk.Frame(self, bg="lightblue", bd=2, relief="solid")
        text_frame.place(relx=0.5, rely=0.45, anchor=tk.CENTER)




        # Title Label
        title_label_line1 = ttk.Label(self, text="Welcome to Driver Drowsiness", style="Title.TLabel")
        title_label_line1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        title_label_line2 = ttk.Label(self, text="Detection System", style="Title.TLabel")
        title_label_line2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        
        # Start Button
        start_button = ttk.Button(self, text="Start", width=20, command=self.start, style="lightBlue.TButton")
        start_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def start(self):
        self.master.title_page.pack_forget()
        self.master.page1.pack(fill="both", expand=True)
        ###############################################################login page##############################

class LoginPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(width=700, height=600, background="blue", relief="solid", borderwidth=2)

        # Load and resize the background image
        image = Image.open("bcg.jpg")
        image = image.resize((1000, 700))
        self.background_image = ImageTk.PhotoImage(image)

        # Display the background image using a label
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        # Username Label and Entry
        self.username_label = ttk.Label(self, text="Username:",font=("Comic Sans MS", 14))
        self.username_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.username_entry = ttk.Entry(self,font=("Arial", 14),style="Blue.TEntry")
        self.username_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        # self.username_entry.config(style="Blue.TEntry")

        # Password Label and Entry
        self.password_label = ttk.Label(self, text="Password:",font=("Comic Sans Ms", 14))
        self.password_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.password_entry = ttk.Entry(self, show="*",font=("Arial", 14),style="Blue.TEntry")
        self.password_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        # self.password_entry.config(style="Blue.TEntry")

        # Configure the style for the blue border
        self.style = ttk.Style()
        self.style.configure("Blue.TEntry", bordercolor="blue", borderwidth=4)

        # Login Button
        self.login_button = ttk.Button(self, text="Login", command=self.login, style="lightBlue.TButton",width=20)
        self.login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, admin!")
            self.pack_forget()
            self.master.page2.pack(fill="both", expand=True)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
################################################################config page#####################################################

class Page2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(width=700, height=600, background="lightblue", relief="solid", borderwidth=2)

         # Load and resize the background image
        image = Image.open("bcg.jpg")
        image = image.resize((1000, 700))
        self.background_image = ImageTk.PhotoImage(image)

        # Display the background image using a label
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        # Label for Page 2
        label = ttk.Label(self, text="Configuration Page", font=("Comic Sans Ms", 24))
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Input fields for data
        self.Account_sid_label = ttk.Label(self, text="Your Account SID",font=("Comic Sans Ms", 14))
        self.Account_sid_label.place(relx=0.3, rely=0.3, anchor=tk.CENTER)
        self.Account_sid_entry = ttk.Entry(self, width=70)
        self.Account_sid_entry.place(relx=0.7, rely=0.3, anchor=tk.CENTER)

        self.Auth_token_label = ttk.Label(self, text="Your Authorization token",font=("Comic Sans Ms", 14))
        self.Auth_token_label.place(relx=0.3, rely=0.4, anchor=tk.CENTER)
        self.Auth_token_entry = ttk.Entry(self, width=70)
        self.Auth_token_entry.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

        self.Twilio_Number_label = ttk.Label(self, text="Your Twilio Number:",font=("Comic Sans Ms", 14))
        self.Twilio_Number_label.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
        self.Twilio_Number_entry = ttk.Entry(self, width=70)
        self.Twilio_Number_entry.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

        self.Recipient_Number_label = ttk.Label(self, text="Recipient Phone Number",font=("Comic Sans Ms", 14))
        self.Recipient_Number_label.place(relx=0.3, rely=0.6, anchor=tk.CENTER)
        self.Recipient_Number_entry = ttk.Entry(self, width=70)
        self.Recipient_Number_entry.place(relx=0.7, rely=0.6, anchor=tk.CENTER)

        # Update button
        self.update_button = ttk.Button(self, text="Update", command=self.update_data, style="lightBlue.TButton",width=20)
        self.update_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def update_data(self):
        global new_account_sid, new_auth_token, new_twilio_phone_number, new_recipient_phone_number
        new_account_sid = self.Account_sid_entry.get()
        new_auth_token = self.Auth_token_entry.get()
        new_twilio_phone_number = self.Twilio_Number_entry.get()
        new_recipient_phone_number = self.Recipient_Number_entry.get()

        conn = sqlite3.connect('test.db')
        print("Opened Database successfully to replace")

        conn.execute("REPLACE INTO COMPANY (id, account_sid, auth_token, twilio_phone_number, recipient_phone_number) \
                  VALUES (?, ?, ?, ?, ?)", (1, new_account_sid, new_auth_token, new_twilio_phone_number, new_recipient_phone_number))

        conn.commit()
        print("Record Created Successfully")
        conn.close() 

        # Process the data or perform any action
        print("Input 1:", new_account_sid)
        print("Input 2:", new_auth_token)
        print("Input 3:",

 new_twilio_phone_number)
        print("Input 4:", new_recipient_phone_number)

if __name__ == "__main__":
    app = TwoPageGUI()
    app.geometry("1000x700")  # Set the window geometry
    app.mainloop()


# Now, the font of the title label on the title page will be set to 'Comic Sans MS'.