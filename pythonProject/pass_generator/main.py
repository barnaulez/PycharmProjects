from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

WHITE = "#ffffff"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def update_json(new_data):
    with open("data.json", mode="r") as f:
        data = json.load(f)
        data.update(new_data)
        dump_json(data)

def dump_json(new_data):
    with open("data.json", mode="w") as f:
        json.dump(new_data, f, indent=4)


def save_file():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning!", message="Hey! Check entered data! \n"
                                                         "Don't left any empty fields!")
    else:
        try:
            update_json(new_data)
        except FileNotFoundError:
            dump_json(new_data)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()

def find_password():
    website = website_input.get()
    try:
        f = open("data.json", mode="r")
    except FileNotFoundError:
        messagebox.showwarning(title="File not found", message="No Data File Found")
    else:
        data = json.load(f)
        if website in data:
            creds = data[website]
            messagebox.showinfo(title=website, message=f"Email: {creds['email']} \n"
                                                       f"Password: {creds['password']}")
        else:
            messagebox.showwarning(title="Data not found", message=f"No details for the {website} exists")
        f.close()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=WHITE)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#-----------------------Labels---------------------------------------#

website_label = Label(text="Website:", bg=WHITE)
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:", bg=WHITE)
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=WHITE)
password_label.grid(row=3, column=0)

#-----------------------Entries--------------------------------------#

website_input = Entry(width=24)
website_input.grid(row=1, column=1, sticky="W")
website_input.focus()

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, sticky="EW")
username_input.insert(0, "your@email.com")

password_input = Entry(width=24)
password_input.grid(row=3, column=1, sticky="W")

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

generate_button = Button(text="Generate Password", width=15, command=pass_gen)
generate_button.grid(row=3, column=2, sticky="E")

add_button = Button(text="Add", width=36, command=save_file)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()