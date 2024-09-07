import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

password = ""

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    # password_list = [new_item for item in list]
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    print(f"Your password is: {password}")
    generated_Password_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def search():
    generated_Password_entry.delete(0,END)
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except:
        messagebox.showinfo(title='not found',message="Data File not Found")
    else:
        website = website_entry.get()
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            pyperclip.copy(password)
            messagebox.showinfo(title="Credentials", message=f"email : {email}\n password : {password}")
            generated_Password_entry.insert(END, string=password)
        else:
            messagebox.showerror(title="not found!",message="Credentials Not Found")

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = generated_Password_entry.get()
    new_data = {
        website : {
            'email' : email,
            'password' : password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Fields", message="Hey You have left some fields Empty!")
    else:
        try:
            file1 = open("data.json",'r')
        except FileNotFoundError:
            file = open('data.json','w')
            json.dump(new_data, file, indent=4)
        else:
            data = json.load(file1)
            data.update(new_data)
            with open('data.json','w') as file2:
                json.dump(data, file2, indent=4)

            print(data)

        # # file.write(f'{website} | {email} | {password}\n')
        website_entry.delete(0, END)
        generated_Password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manger")
# window.minsize(400,300)
window.config(pady=50, padx=50)
canvas = Canvas(width=200, height=200)
image_file = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image_file)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, string="Muzirkhan13@gmail.com")
generated_Password_entry = Entry(width=21)
generated_Password_entry.grid(row=3, column=1)

search_button = Button(text='Search',command=search)
search_button.grid(row=1,column=2)
generate_Password_button = Button(text="Generate Password", highlightthickness=1, command=generate_password)
generate_Password_button.grid(row=3, column=2)
add_password_button = Button(text="Add", width=36, command=save)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
