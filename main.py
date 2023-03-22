from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_nums = [random.choice(numbers) for _ in range(nr_symbols)]
    password_symbols = [random.choice(symbols) for _ in range(nr_numbers)]

    password_list = password_letters + password_nums + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_used_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_credentials():
    website_name = website_name_entry.get()
    user_id = email_used_entry.get()
    user_password = password_used_entry.get()

    data_to_dict = {
        website_name: {
            "username": user_id,
            "password": user_password
        }

    }

    if len(website_name) == 0 or len(user_id) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Something went wrong", message="Please make sure you haven't left any fiel empty")
    else:
        is_confirmed = messagebox.askokcancel(title=website_name,
                                            message=f"These are the credentials entered: \nUsername:" 
                                            f"{user_id} \nPassword: {user_password}")
        
        if is_confirmed:
            try:
                with open("data.json", "r") as data_file:
                    #Reading data from JSON file
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    print("Inside exception")
                    #Saving updated data
                    json.dump(data_to_dict, data_file, indent=4)
            else:
                    #Updating old data with new one
                    data.update(data_to_dict)

                    with open("data.json", "w") as data_file:
                         json.dump(data_to_dict, data_file, indent=4)
            finally:
                    print("on finally")
                    #Clearing the fields out for next entry
                    website_name_entry.delete(0, END)
                    email_used_entry.delete(0, END)
                    password_used_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Creating all labels for UI and setting up grid location
website_name_label = Label(text="Website:")
website_name_label.grid(row=1, column=0)

email_used_label = Label(text="Email/Username:")
email_used_label.grid(row=2, column=0)

password_used_label = Label(text="Password:")
password_used_label.grid(row=3, column=0)

#Creating all the etries and setting up grid location
website_name_entry = Entry(width=41)
website_name_entry.grid(row=1, column=1, columnspan=2)
website_name_entry.focus()

email_used_entry = Entry(width=41)
email_used_entry.grid(row=2, column=1,  columnspan=2)

password_used_entry = Entry(width=24)
password_used_entry.grid(row=3, column=1)

#Creating buttons and setting up grid location
generate_password_button = Button(text="Generate Passwd", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_entry_button = Button(text="Add", width=35, command=save_credentials)
add_entry_button.grid(row=4, column=1, columnspan=2)

window.mainloop()