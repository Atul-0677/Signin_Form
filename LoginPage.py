import email

from database import *
create_database()
# save_user("atul@gmail.com", "123456")
show_users()
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re

# ==========================
# Email Validation
# ==========================
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return re.match(pattern, email)

# ==========================
# Login Function
# ==========================
def handle_login():

    email = email_input.get().strip()
    password = password_input.get().strip()

    # Email Empty
    if email == "":
        messagebox.showerror(
            "Email Error",
            "Please enter your email."
        )
        return

    # Email Validation
    if not is_valid_email(email):
        messagebox.showerror(
            "Invalid Email",
            "Please enter a valid Gmail address.\nExample: atul@gmail.com"
        )
        return

    # Password Empty
    if password == "":
        messagebox.showerror(
            "Password Error",
            "Please enter your password."
        )
        return

    # Password Length Check
    if len(password) < 6:
        messagebox.showerror(
            "Weak Password",
            "Password must be at least 6 characters."
        )
        return

    print("Email entered:", email)
    print("Password entered:", password)
    user = check_login(email, password)
    print("Database result:", user)
    if user:
        messagebox.showinfo(
        "Success",
        f"Welcome {email}"
    )
    # Clear fields after successful login
        email_input.delete(0, END)
        password_input.delete(0, END)

    else:
        messagebox.showerror(
        "Login Failed",
        "Invalid Email or Password"
    )

# ==========================
# Show/Hide Password
# ==========================
def toggle_password():

    if show_password.get() == 1:
        password_input.config(show="")
    else:
        password_input.config(show="*")

# ==========================
# Main Window
# ==========================
root = Tk()

root.title("Flipkart Login")
root.geometry("400x550")
root.configure(bg="#0096DC")
root.resizable(False, False)

# ==========================
# Icon
# ==========================
try:
    root.iconbitmap("form-icon.png")
except:
    pass

# ==========================
# Logo
# ==========================
try:
    img = Image.open("Flipkart-logo1.jpg")
    img = img.resize((100, 100))
    photo = ImageTk.PhotoImage(img)

    logo_label = Label(
        root,
        image=photo,
        bg="#0096DC"
    )
    logo_label.pack(pady=20)

except:
    logo_label = Label(
        root,
        text="Flipkart",
        font=("Verdana", 24, "bold"),
        bg="#0096DC",
        fg="white"
    )
    logo_label.pack(pady=20)

# # ==========================
# # Heading
# # ==========================
heading = Label(
    root,
    text="Login Form",
    font=("Verdana", 18, "bold"),
    bg="#0096DC",
    fg="white"
)

heading.pack(pady=10)

# ==========================
# Email Label
# ==========================
email_label = Label(
    root,
    text="Email Address",
    font=("Verdana", 12),
    bg="#0096DC",
    fg="white"
)

email_label.pack(pady=(20, 5))

# ==========================
# Email Entry
# ==========================
email_input = Entry(
    root,
    width=30,
    font=("Arial", 12)
)

email_input.pack(ipady=5)

# ==========================
# Password Label
# ==========================
password_label = Label(
    root,
    text="Password",
    font=("Verdana", 12),
    bg="#0096DC",
    fg="white"
)

password_label.pack(pady=(20, 5))

# ==========================
# Password Entry
# ==========================
password_input = Entry(
    root,
    width=30,
    font=("Arial", 12),
    show="*"
)

password_input.pack(ipady=5)

# ==========================
# Show Password Checkbox
# ==========================
show_password = IntVar(value=0)

show_password_checkbox = Checkbutton(
    root,
    text="Show Password",
    variable=show_password,
    command=toggle_password,
    bg="#0096DC",
    # fg="white",
    activebackground="#0096DC",
    # activeforeground="white",
    # selectcolor="white"
)

show_password_checkbox.pack(pady=10)

# ==========================
# Login Button
# ==========================
login_btn = Button(
    root,
    text="Login",
    width=15,
    font=("Verdana", 12, "bold"),
    bg="yellow",
    command=handle_login
)

login_btn.pack(pady=20)

# ==========================
# Sign Up Link
import os

def open_signup():
    os.system("python signin.py")

Button(
    root,
    text="Create New Account",
    command=open_signup,
    width=17,
    font=("Verdana",8, "bold"),
    bg="#0096DC",
    # fg="#0096DC",
    fg="white",
    # relief="solid"
    ).pack()



# ==========================
# Footer
# ==========================
footer = Label(
    root,
    text="Created Using Python Tkinter",
    font=("Arial", 9),
    bg="#0096DC",
    fg="white"
)

footer.pack(side=BOTTOM, pady=10)

# ==========================
# Run App
# ==========================
root.mainloop()