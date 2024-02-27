from tkinter import *
root=Tk()
root.title("Create New Account")
root.geometry("750x520")
root.resizable(0,0)

def generate_ac_no():
    import random
    import string
    random_number = ' '.join(str(random.randint(0, 9))for i in range(11))
    alphabet = random.choice(string.ascii_uppercase)
    account_number = "0 0 "+(random_number) + " "+alphabet
    account_number_entry.delete(0, END)
    account_number_entry.insert(0,account_number)

def clear():
    account_number_entry.delete(0, END)
    name_entry.delete(0, END)
    dob_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_number_entry.delete(0, END)
    address_entry.delete(0, END)

#Labels
heading_label=Label(root, text="Create New Account",font=("Arial", 20, "bold"))
heading_label.place(x=250, y=20)

account_number_label=Label(root, text="Account Number : ",font=("Arial ",12,"bold"))
account_number_label.place(x=100,y=120)

name_label=Label(root, text="Name : ",font=("Arial ",12,"bold"))
name_label.place(x=100,y=160)

gender_label=Label(root, text="Select Gender : ",font=("Arial ",12,"bold"))
gender_label.place(x=100,y=200)

gender = StringVar(value="F")

radio1 = Radiobutton(root, text="Male", font=("Arial ", 10), variable=gender, value="M")
radio1.place(x=250, y=200)
radio1.select()

radio2 = Radiobutton(root, text="Female", font=("Arial ", 10), variable=gender, value="F")
radio2.place(x=320, y=200)
radio2.deselect()

dob_label=Label(root, text="DOB : ",font=("Arial ",12,"bold"))
dob_label.place(x=100,y=240)

email_label=Label(root, text="Email : ",font=("Arial ",12,"bold"))
email_label.place(x=100,y=280)

phone_number_label=Label(root, text="Phone Number : ",font=("Arial ",12,"bold"))
phone_number_label.place(x=100,y=320)

address_label=Label(root, text="Address : ",font=("Arial ",12,"bold"))
address_label.place(x=100,y=360)

#Entry Boxes
account_number_entry=Entry(root,width=30)
account_number_entry.place(x=250,y=120)

name_entry=Entry(root,width=30)
name_entry.place(x=250,y=160)

dob_entry=Entry(root,width=30)
dob_entry.place(x=250,y=240)

email_entry=Entry(root,width=30)
email_entry.place(x=250,y=280)

phone_number_entry=Entry(root,width=30)
phone_number_entry.place(x=250,y=320)

address_entry=Entry(root,width=30)
address_entry.place(x=250,y=360)

#Buttons
generate_ac_no_btn=Button(root, text=("Generate AC No"), font=("Arial Bold", 12), fg="white", bg="#00BFFF", width=15, cursor="hand2", command=generate_ac_no)
generate_ac_no_btn.place(x=100, y=420)

submit_btn=Button(root, text=("Submit"), font=("Arial Bold", 12),fg="white",bg="green",width=10,cursor="hand2",command=submit)
submit_btn.place(x=300,y=420)

clear_btn=Button(root, text=("Clear"), font=("Arial Bold", 12),fg="white",bg="red",width=10,cursor="hand2",command=clear)
clear_btn.place(x=450,y=420)

root.mainloop()
