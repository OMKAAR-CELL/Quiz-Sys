from tkinter import *

# List of subjects for the quiz
quiz_subjects = [
    "General Knowledge",
    "Science",
    "Mathematics",
    "History",
    "Geography",
    "Literature",
    "Technology",
    "Sports",
    "Entertainment",
    "Mythology",
    "Current Affairs",
    "Pop Culture"
]



qno=1


fon="vendana"
root = Tk()
root.geometry("900x600")
root.configure(background="#E9EDF1")
root.resizable(0, 0)


# Frames
Welcome = Frame(root, background="#E9EDF1")
Login = Frame(root, background="#E9EDF1")
Signup = Frame(root, background="#E9EDF1")
Declar = Frame(root, background="#E9EDF1")
Question = Frame(root, background="#E9EDF1")

for frame in (Welcome, Signup, Login,Declar,Question):
    frame.grid(row=0, column=0, sticky="nsew")

def show_frame(frame):
    frame.tkraise()

# Show the Welcome page initially
show_frame(Welcome)



# Welcome Page
welcome_label = Label(
    Welcome, text="Welcome to Quiz", font=(fon, 36, "bold"), bg="#E9EDF1"
)
welcome_label.pack(pady=95,padx=250)  # Centered horizontally

play_btn = Button(
    Welcome,
    text="Play",
    font=(fon, 20),
    width=15,
    height=2,
    bg="#D6DBDF",
    command=lambda: show_frame(Signup),
)
play_btn.pack(pady=100)  # Centered below the label



# Sign Up Page
signup_label = Label(
    Signup, text="Sign Up Page", font=(fon, 36, "bold"), bg="#E9EDF1"
)
signup_label.pack(pady=9,padx=250)  # Centered horizontally

signup_username_txt=Label(
    Signup,
    text="username",
    font=(fon,28),
    bg="#E9EDF1"
)
signup_username_txt.pack(pady=(79,0),padx=(250,0),anchor="w")

signup_username_ent=Entry(
    Signup,
    width=20,
    font=(fon,22)
)
signup_username_ent.pack(pady=(13,0),padx=0)

signup_password_txt=Label(
    Signup,
    text="password",
    font=(fon,28),
    bg="#E9EDF1"
)
signup_password_txt.pack(pady=(25,0),padx=(250,0),anchor="w")

signup_password_ent=Entry(
    Signup,
    width=20,
    font=(fon,22)
)
signup_password_ent.pack(pady=(13,10),padx=0)

subm_btn=Button(
    Signup,
    text="Submit",
    bg="#5582BE",
    width=20,
    font=(fon,20),
    command=lambda :show_frame(Declar)
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
login_label.pack(pady=9,padx=250)  # Centered horizontally

login_username_txt=Label(
    Login,
    text="username",
    font=(fon,28),
    bg="#E9EDF1"
)
login_username_txt.pack(pady=(79,0),padx=(250,0),anchor="w")

login_username_ent=Entry(
    Login,
    width=20,
    font=(fon,22)
)
login_username_ent.pack(pady=(13,0),padx=0)

login_password_txt=Label(
    Login,
    text="password",
    font=(fon,28),
    bg="#E9EDF1"
)
login_password_txt.pack(pady=(25,0),padx=(250,0),anchor="w")

login_password_ent=Entry(
    Login,
    width=20,
    font=(fon,22)
)
login_password_ent.pack(pady=(13,10),padx=0)

sub_btn=Button(
    Login,
    text="Submit",
    bg="#5582BE",
    width=20,
    font=(fon,20),
    command=lambda :show_frame(Declar)
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



#Declare

# Declare Frame
declar_label = Label(Declar, text="Choose the subject", font=(fon, 45), bg="#E9EDF1")
declar_label.pack()

btnframe1 = Frame(Declar, bg="#E9EDF1")
btnframe1.pack(pady=(70, 0))

# Buttons with symmetrical distance using grid
btn1 = Button(btnframe1, text=str(quiz_subjects[0]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :show_frame(Question))
btn1.grid(row=0, column=0, padx=20, pady=30)

btn2 = Button(btnframe1, text=str(quiz_subjects[1]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :show_frame(Question))
btn2.grid(row=0, column=1, padx=20, pady=30)

btn3 = Button(btnframe1, text=str(quiz_subjects[2]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :show_frame(Question))
btn3.grid(row=0, column=2, padx=20, pady=30)

btn4 = Button(btnframe1, text=str(quiz_subjects[3]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :show_frame(Question))
btn4.grid(row=1, column=0, padx=20, pady=30)

btn5 = Button(btnframe1, text=str(quiz_subjects[4]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :show_frame(Question))
btn5.grid(row=1, column=1, padx=20, pady=30)

btn6 = Button(btnframe1, text=str(quiz_subjects[5]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :show_frame(Question))
btn6.grid(row=1, column=2, padx=20, pady=30)

btn7 = Button(btnframe1, text=str(quiz_subjects[6]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :show_frame(Question))
btn7.grid(row=2, column=0, padx=20, pady=30)

btn8 = Button(btnframe1, text=str(quiz_subjects[7]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :show_frame(Question))
btn8.grid(row=2, column=1, padx=20, pady=30)

btn9 = Button(btnframe1, text=str(quiz_subjects[8]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :show_frame(Question))
btn9.grid(row=2, column=2, padx=20, pady=30)

btn10 = Button(btnframe1, text=str(quiz_subjects[9]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :show_frame(Question))
btn10.grid(row=3, column=0, padx=20, pady=30)

btn11 = Button(btnframe1, text=str(quiz_subjects[10]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :show_frame(Question))
btn11.grid(row=3, column=1, padx=20, pady=30)

btn12 = Button(btnframe1, text=str(quiz_subjects[11]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :show_frame(Question))
btn12.grid(row=3, column=2, padx=20, pady=30)




#Question 
Question_label=Label(Question,text=str(qno)+". Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sunt temporibus quisquam iusto minima veniam quae, sed corporis adipisci suscipit quibusdam",bg='#E9EDF1',font=(fon,22),wraplength=900,justify="left")
Question_label.pack(anchor='w',padx=(4,6),pady=(10,5))

optionframe=Frame(Question,bg="#E9EDF1")
optionframe.pack(padx=(120,0),anchor='w',pady=(120,0))

opt1=Button(optionframe,text="Option 1",font=(fon,18),width=17)
opt1.grid(row=0,column=0)

opt2=Button(optionframe,text="Option 2",font=(fon,18),width=17)
opt2.grid(row=0,column=2,padx=(120,0))

opt3=Button(optionframe,text="Option 3",font=(fon,18),width=17)
opt3.grid(row=1,column=0,pady=(45,0))

opt4=Button(optionframe,text="Option 4",font=(fon,18),width=17)
opt4.grid(row=1,column=2,padx=(120,0),pady=(45,0))


root.mainloop()
