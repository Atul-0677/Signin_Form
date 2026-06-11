from cProfile import label
import os
from tkinter import *
from tkinter import messagebox
from database import *
from PIL import Image, ImageTk

create_database()
show_users()

# ==========================
# Sign Up Function
# ==========================
def handle_signup():

    email = email_input.get().strip()
    password = password_input.get().strip()

    if email == "":
        messagebox.showerror(
            "Error",
            "Please enter email"
        )
        return

    if password == "":
        messagebox.showerror(
            "Error",
            "Please enter password"
        )
        return

    result = save_user(email, password)

    if result:
        messagebox.showinfo(
            "Success",
            "Account Created Successfully"
        )

        email_input.delete(0, END)
        password_input.delete(0, END)

    else:
        messagebox.showerror(
            "Error",
            "Email already exists"
        )

# ==========================
# Window
# ==========================
root = Tk()

root.title("Flipkart Sign In")
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

# ==========================
# Heading
# ==========================
heading = Label(
    root,
    text="Signin Form",
    font=("Verdana", 18, "bold"),
    bg="#0096DC",
    fg="white"
)
heading.pack(pady=10)

# ==========================
# Email
# ==========================
email_Label = Label(
    root,
    text="Email Address",
    font=("Verdana", 12),
    bg="#0096DC",
    fg="white"
)
email_Label.pack(pady=(20, 5))

email_input = Entry(
    root,
    width=30
)

email_input.pack()

# ==========================
# Password
# ==========================
Label(
    root,
    text="Password",
    font=("Verdana", 12),
    bg="#0096DC",
    fg="white"
).pack(pady=10)

password_input = Entry(
    root,
    width=30,
    show="*"
)

password_input.pack()

# ==========================
# Show/Hide Password
# ==========================
def toggle_password():

    if show_password.get() == 1:
        password_input.config(show="")
    else:
        password_input.config(show="*")


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
# Sign Up Button
# ==========================
signup_btn = Button(
    root,
    text="Create Account",
    command=handle_signup,
    font=("Verdana", 10),
    bg="#FB641B",
    fg="white",
    activebackground="#E85D19",
    activeforeground="white",
    cursor="hand2",
    relief="flat",
    bd=0,
    width=16,
    height=1
)

signup_btn.pack(pady=25)

# ==========================
# Hover Effects for Sign Up Button
def signup_enter(event):
    signup_btn.config(bg="#1C5FD4")

def signup_leave(event):
    signup_btn.config(bg="#2874F0")

signup_btn.bind("<Enter>", signup_enter)
signup_btn.bind("<Leave>", signup_leave)

# ==========================
# Already have an account? Login
# ==========================
def open_login():
    os.system("python LoginPage.py")
login_label = Label(
    root,
    text="Already have an account? Login",
    font=("Verdana", 9, "underline"),
    fg="white",
    bg="#0096DC",
    cursor="hand2"
)
login_label.pack(pady=5)

def login_enter(event):
    login_label.config(fg="yellow")

def login_leave(event):
    login_label.config(fg="white")

login_label.bind("<Enter>", login_enter)
login_label.bind("<Leave>", login_leave)
login_label.bind("<Button-1>", lambda e: open_login())

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

root.mainloop()