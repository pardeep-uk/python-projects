from tkinter import messagebox
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail:{email} \nPassword: {password} \n Is it ok to save?")
    
    if len(website) == 0 or len (password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you have not left any fields empty.")
    else:
        if is_ok:
            with open("C:/Users/pardeep.singh02/Desktop/python-projects/python-projects/python-projects/password-manager/data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="C:/Users/pardeep.singh02/Desktop/python-projects/python-projects/python-projects/password-manager/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=1,column=1, columnspan=2)

email_label = Label(text="Username/Email")
email_label.grid(row=2, column=0)
email_entry = Entry(width=40)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(END,"pardeepsingh@gmail.com")

password_label = Label(text="password")
password_label.grid(row=3, column=0)
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)
password_button = Button(text="Genrate Password")
password_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36, command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()