from tkinter import *
root = Tk()
root.config(bg="gray20")
root.title("Bank Management System")
root.geometry("1500x700")
root.resizable(0, 0)

lbl=Label(root,text="Bank Management System", font=("Arial Bold",50),bg="gray20",fg="white")
lbl.place(x=350,y=20)

def create_account():
    import create_new_account

def deposit_amount():
    import deposit_amount

def withdraw_amount():
    import withdraw_amount        

def check_balance():
    import check_balance

def delete_account():
    import delete_account
    
def retrieve_data():
    import customer_details

def update_account():
    import update_account

def exit():
    root.destroy()


create_btn=Button(root,text="Create New Account",font=("Arial Bold",20),fg="white",bg="blue",width=17,cursor="hand2",command=create_account)
create_btn.place(x=200,y=200)

deposite_btn=Button(root,text="Deposit Amount",font=("Arial Bold",20),fg="white",bg="blue",width=17,cursor="hand2",command=deposit_amount)
deposite_btn.place(x=200,y=300)

withdraw_btn=Button(root,text="Withdraw Amount",font=("Arial Bold",20),fg="white",bg="blue",width=17,cursor="hand2",command=withdraw_amount)
withdraw_btn.place(x=200,y=400)

check_balance_btn=Button(root,text="Check Balance",font=("Arial Bold",20),fg="white",bg="blue",width=17,cursor="hand2",command=check_balance)
check_balance_btn.place(x=200,y=500)

retrieve_btn=Button(root,text="Customer Details",font=("Arial Bold",20),fg="white",bg="blue",width=17,cursor="hand2",command=retrieve_data)
retrieve_btn.place(x=1000,y=200)

delete_btn=Button(root,text="Delete Account",font=("Arial Bold",20),fg="white",bg="blue",width=17,cursor="hand2",command=delete_account)
delete_btn.place(x=1000,y=300)


update_btn=Button(root,text="Update Account",font=("Arial Bold",20),fg="white",bg="blue",width=17,cursor="hand2",command=update_account)
update_btn.place(x=1000,y=400)

exit_btn=Button(root,text="Exit",font=("Arial Bold",20),fg="white",bg="red",width=17,cursor="hand2",command=exit)
exit_btn.place(x=1000,y=500)


root.mainloop()


