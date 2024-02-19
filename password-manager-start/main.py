#imports
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    char_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    num_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = char_list + symbol_list + num_list
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(text=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_name_input.get()
    email_uname = email_uname_input.get()
    password = password_input.get()

    if len(website) != 0 and len(password) != 0:
        password_data = f"{website} | {email_uname} | {password}\n"
        is_okay = messagebox.askokcancel(title=website,
                                         message=f"These are the details entered: \nEmail: {email_uname} \nPassword: {password}"
                                                 f" \nIs it okay to save?")
        if is_okay:
            with open(file="passwords_details.txt", mode="a") as output_file:
                output_file.write(password_data)
                # erasing values from all the fields
                website_name_input.delete(0, END)
                password_input.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
#window
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

#creating a canvas
canvas = Canvas(window, width=200, height=200)
logo_image = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

#creating labels, text fields and Buttons
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_name_input = Entry(width=52)
website_name_input.focus()
website_name_input.grid(row=1, column=1, columnspan=2)

email_uname_label = Label(text="Email/Username:")
email_uname_label.grid(row=2, column=0)

email_uname_input = Entry(width=52)
email_uname_input.insert(0,"alexandraa@email.com")
email_uname_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=33)
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
