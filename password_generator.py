import random
import string
import tkinter as tk

def generate_password(length):
    # define the character sets to be used for generating password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # combine all the character sets
    all_chars = lowercase + uppercase + digits + symbols

    # generate the password by randomly selecting characters from the combined set
    password = ''.join(random.sample(all_chars, length))

    return password

def generate_password_ui():
    # create a window
    window = tk.Tk()
    window.title("Password Generator")

    # create a label and entry for password length
    length_label = tk.Label(window, text="Enter password length:")
    length_label.pack()
    length_entry = tk.Entry(window)
    length_entry.pack()

    # create a label for the generated password
    password_label = tk.Label(window, text="Generated Password:")
    password_label.pack()

    # create a function to generate password on button click
    def generate():
        length = int(length_entry.get())
        password = generate_password(length)
        password_label.config(text=password)

    # create a button to generate password
    generate_button = tk.Button(window, text="Generate", command=generate)
    generate_button.pack()

    # run the window
    window.mainloop()

# run the program
generate_password_ui()
