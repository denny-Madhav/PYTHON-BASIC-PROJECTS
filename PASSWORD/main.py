from tkinter import *
from tkinter import messagebox
import pyperclip
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for item in range(nr_letters)]
    password_number = [random.choice(numbers) for item in range(nr_numbers)]
    password_symblos = [random.choice(symbols) for item in range(nr_symbols)]

    password_list = password_letter + password_number + password_symblos
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site_name = website_input.get()
    Uid = user_name_input.get()
    password = password_input.get()

    if len(site_name) == 0 or len(password) == 0:
        messagebox.showwarning(title="details not entered",message="Please enter all the necessary details")
    else:
        haa_ya_naah = messagebox.askokcancel(title = site_name,message =f"These are the details entered:\nEmail: {Uid}\nPassword: {password}\n\nIs it okay to save.")

        if haa_ya_naah:
            saving = open("data.txt", "a")
            saving.write(f" \n******\nSITE = {site_name} || ID = {Uid} || PASS = {password} \n")
            website_input.delete(0, END)
            password_input.delete(0, END)
            saving.close()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30,pady=30)


canvas = Canvas(width= 200, height=200)
logoIMG = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= logoIMG)
canvas.grid(row=0,column=1)


web_site = Label(text="Website :")
web_site.grid(row=1,column=0)
user_name = Label(text="User ID :")
user_name.grid(row=2,column=0)
password_label = Label(text="Password :")
password_label.grid(row=3,column=0)


website_input = Entry(width=35)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()
user_name_input = Entry(width=35)
user_name_input.grid(row=2,column=1,columnspan=2)
user_name_input.insert(0,"Nallidennny@gmail.com")
password_input = Entry(width=35)
password_input.grid(row=3,column=1)

generate_button=Button(text="Generate Password",width=30,command=generate)
generate_button.grid(row=4,column=1,columnspan=2)
save_button=Button(text="Save Deatils",width=30,command=save)
save_button.grid(row=5,column=1,columnspan=2)














window.mainloop()