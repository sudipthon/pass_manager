# import pyperclip
from tkinter import messagebox
from tkinter import *
import random
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters=['a', 'b', 'c', 'd', 'e', 'f',' 0','1','2','3','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','#','$', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','4','5','6','7','8','9','!','#','$','%','&','*']
def generate_password():
    a=''
    for i in range (10):
        y=random.choice(letters)
        a+=y
    password_entry.insert(0,a)

# # ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    # checking if the user wants to save data through popup
    if len(website)!=0 or len(password)!=0 and len(email)!=0:
        is_ok=messagebox.askokcancel(title="Title",message=f"these are the details entered:\nWebsite:{website}\nEmail:{email}\nPassword:{password}\n Is it ok to save?")
        if is_ok:
    
            #saving the user data
            with open("data.txt","a") as data:
                data.write(f"{website} | {email} | {password}\n")
             #saving pass in clipboard   
            pyperclip.copy(password)
            #clearing fields
        website_entry.delete(0,END)
        password_entry.delete(0,END)
    else:
        messagebox.showinfo(title="Empty field",message="You haven't entered data in all fields")

# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)


canva=Canvas(width=200,height=200)
pic=PhotoImage(file="logo.png")
canva.create_image(100,100,image=pic)
canva.grid(column=1,row=0)

website_label=Label(text="Webste:")
website_label.grid(column=0,row=1)
email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label=Label(text="Password:")
password_label.grid(column=0,row=3)
password_label.config(padx=0)

website_entry=Entry(width=40)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=40)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"sudip00kc@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(column=1,row=3)

generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2,row=3)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)
 
window.mainloop()
