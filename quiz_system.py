from tkinter import *

fon="Inter"
root = Tk()
root.geometry("900x600")
root.configure(background="#E9EDF1")
root.resizable(0, 0)

# Frames
Welcome = Frame(root, background="#E9EDF1")
Login = Frame(root, background="#E9EDF1")
Signup = Frame(root, background="#E9EDF1")

for frame in (Welcome, Signup, Login):
    frame.grid(row=0, column=0, sticky="nsew")

def show_frame(frame):
    frame.tkraise()

# Show the Welcome page initially
show_frame(Welcome)

# Welcome Page
welcome_label = Label(
    Welcome, text="Welcome to Quiz", font=("Verdana", 36, "bold"), bg="#E9EDF1"
)
welcome_label.pack(pady=9,padx=200)  # Centered horizontally

play_btn = Button(
    Welcome,
    text="Play",
    font=(fon, 20),
    width=15,
    height=2,
    bg="#D6DBDF",
    command=lambda: show_frame(Signup),
)
play_btn.pack(pady=140)  # Centered below the label

# Sign Up Page
signup_label = Label(
    Signup, text="Sign Up Page", font=(fon, 36, "bold"), bg="#E9EDF1"
)
signup_label.pack(pady=9,padx=200)  # Centered horizontally

username_txt=Label(
    Signup,
    text="username",
    font=(fon,28),
    bg="#E9EDF1"
)
username_txt.pack(pady=(79,0),padx=(250,0),anchor="w")

username_ent=Entry(
    Signup,
    width=20,
    font=(fon,22)
)
username_ent.pack(pady=(13,0),padx=0)

password_txt=Label(
    Signup,
    text="password",
    font=(fon,28),
    bg="#E9EDF1"
)
password_txt.pack(pady=(25,0),padx=(250,0),anchor="w")

username_ent=Entry(
    Signup,
    width=20,
    font=(fon,22)
)
username_ent.pack(pady=(13,10),padx=0)

subm_btn=Button(
    Signup,
    text="Submit",
    bg="#5582BE",
    width=20,
    font=(fon,20)
)
subm_btn.pack(pady=(20,90))


login_frame = Frame(Signup, bg="#E9EDF1")
login_frame.pack(pady=(10, 0))

login_txt=Label(
    login_frame,
    text="already have credentials",
    bg="#E9EDF1",
    fg="#5582BE",
    font=(fon,12)
)
login_txt.pack(side="left", padx=(0, 5))

login_btn=Button(
    login_frame,
    text="login",
    command=lambda: show_frame(Login)
)
login_btn.pack(side="left")


#Login
login_label = Label(
    Login, text="login Page", font=(fon, 36, "bold"), bg="#E9EDF1"
)
login_label.pack(pady=9,padx=200)  # Centered horizontally

username_txt=Label(
    Login,
    text="username",
    font=(fon,28),
    bg="#E9EDF1"
)
username_txt.pack(pady=(79,0),padx=(250,0),anchor="w")

username_ent=Entry(
    Login,
    width=20,
    font=(fon,22)
)
username_ent.pack(pady=(13,0),padx=0)

password_txt=Label(
    Login,
    text="password",
    font=(fon,28),
    bg="#E9EDF1"
)
password_txt.pack(pady=(25,0),padx=(250,0),anchor="w")

username_ent=Entry(
    Login,
    width=20,
    font=(fon,22)
)
username_ent.pack(pady=(13,10),padx=0)

sub_btn=Button(
    Login,
    text="Submit",
    bg="#5582BE",
    width=20,
    font=(fon,20)
)
sub_btn.pack(pady=(20,90))

signup_frame = Frame(Login, bg="#E9EDF1")
signup_frame.pack(pady=(10, 0))

signup_txt=Label(
    signup_frame,
    text="Don't have credentials",
    bg="#E9EDF1",
    fg="#5582BE",
    font=(fon,12)
)
signup_txt.pack(side="left", padx=(0, 5))

signup_btn=Button(
    signup_frame,
    text="signup",
    command=lambda: show_frame(Signup)
)

signup_btn.pack(side="left")


root.mainloop()

