import smtplib
from tkinter import *


def send_message():
    reciever_email = address.get()

    email_body_txt = email_body.get()

    print(reciever_email, email_body_txt)

    sender_email = "xploradora0@gmail.com"

    sender_password = "sachin16112000"

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender_email ,  sender_password)

    print("Login successful")

    server.sendmail(sender_email, reciever_email , email_body_txt)

    print("Message sent")






app = Tk()

app.geometry("500x500")

app.title("Python Mail Send App")

heading = Label(text="Python Email Sending App", bg="lightblue", fg="black", font="10", width="500", height="3")

heading.pack()

address_field = Label(text="Recipient Address :")
email_body_field = Label(text="Message :")

address_field.place(x=15, y=70)
email_body_field.place(x=15, y=140)

address = StringVar()
email_body = StringVar()

address_entry = Entry(textvariable=address, width="30")
email_body_entry = Entry(textvariable=email_body, width="30")

address_entry.place(x=15, y=100)
email_body_entry.place(x=15, y=180)

button = Button(app, text="Send Message", command=send_message, width="30", height="2", bg="green")

button.place(x=15, y=220)

mainloop()
