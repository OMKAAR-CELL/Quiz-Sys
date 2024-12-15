from tkinter import *
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image,ImageTk


username=NONE


#helping Functions
def get_length(df,sub,user):
    id_df=df[(df['Subject']==sub) & (df['Username']==user)]
    length=len(id_df)
    ls=[j for j in range(1,length+1)]
    return ls

def get_subject(df,sub,user):
    Scoredf=df[(df['Subject']==sub) & (df['Username']==user)]
    Scoredf=Scoredf['Score']
    
    return Scoredf
    
def get_max(ls, df, user):
    results = []
    for index in range(len(ls)):
        Sub_max = df[(df['Subject'] == ls[index]) & (df['Username'] == user)]
        if not Sub_max.empty:
            results.append(max(Sub_max['Score']))
        else:
            results.append(0)  # Default score if no matching records
    return results


#Chart creating functions
def create_piechart(score):
    plt.pie([score,10-score],labels=["Right","Wrong"])
    plt.legend()
    plt.savefig('piechart')
    plt.close()

def create_barchart(quiz_subjects,user_progress_data,username):
    sub=["G.K","Science","Maths","History","Geo","Lit.","Tech","Sports","Ent.","Mytho","C.A","Pop Cul."]
    plt.barh(sub,get_max(quiz_subjects,user_progress_data,username))
    plt.yticks(fontsize=8)
    plt.ylabel('Subjects')
    plt.xlabel('Maximum Score')
    plt.savefig('Barchart')
    plt.close()
    
def create_linechart(subject,user_progress_data,username):
    plt.plot(get_length(user_progress_data, subject, username), get_subject(user_progress_data, subject, username), label=subject)
    plt.legend()
    plt.savefig('LineChart')
    plt.close()
    

#button function & backend
def add_user(): #Signing Up and adding user in respective csv file
    global username
    username = signup_username_ent.get().strip()
    password = signup_password_ent.get().strip()

    if not username or not password:
        messagebox.showwarning('Fill the fields', 'Please enter both username and password.')
        return

    if username in user_pass_data['username'].values:
        messagebox.showinfo('Username already exists', f"Username '{username}' is already taken. Please choose a different one.")
    else:
        user_pass_data.loc[len(user_pass_data)] = [username, password]
        user_pass_data.to_csv('users.csv', index=False)
        signup_username_ent.delete(0, END)
        signup_password_ent.delete(0, END)
        messagebox.showinfo('Success', 'User registered successfully!')
        show_frame(Login)


def login_user(): #Logingin in user
    global username
    username = login_username_ent.get().strip()
    password = login_password_ent.get().strip()

    if not username or not password:
        messagebox.showwarning('Fill the fields', 'Please enter both username and password.')
        return
    
    user_row = user_pass_data[user_pass_data['username'] == username]
    if not user_row.empty and user_row.iloc[0]['password'] == password:
        messagebox.showinfo('Success', 'Login successful!')
        show_frame(Declar)
    else:
        messagebox.showwarning('login failed','please enter correct username and password')
         
    
def increase_qno(): #increasing qustion number
    global qno
    qno+=1


def Show_Question(id): #Showing question for the first instance
    global qno
    global globalid
    global section_question
    
    globalid = id  # Update the global ID for the subject

    # Filter questions for the selected subject
    section_question = questions_data[questions_data['Subject'] == id].sample(10).reset_index(drop=True)

    # Check if `qno` is within valid range
    question_text = f"{qno}. {section_question.loc[qno - 1, 'Question']}"
    Question_label.configure(text=question_text)

    # Update options
    opt1.configure(text=section_question.loc[qno - 1, "OptionA"])
    opt2.configure(text=section_question.loc[qno - 1, "OptionB"])
    opt3.configure(text=section_question.loc[qno - 1, "OptionC"])
    opt4.configure(text=section_question.loc[qno - 1, "OptionD"])
       
def show_Questions_forcont(): #Showing question after first instance
    global qno
    global section_question
    
    if qno<=len(section_question):
        question_text = f"{qno}. {section_question.loc[qno - 1, 'Question']}"
        Question_label.configure(text=question_text)

                # Update options
        opt1.configure(text=section_question.loc[qno - 1, "OptionA"])
        opt2.configure(text=section_question.loc[qno - 1, "OptionB"])
        opt3.configure(text=section_question.loc[qno - 1, "OptionC"])
        opt4.configure(text=section_question.loc[qno - 1, "OptionD"])
        
        opt1.configure(bg='#2eff70')
        opt2.configure(bg='#2eff70')
        opt3.configure(bg='#2eff70')
        opt4.configure(bg='#2eff70')
    else:
        Progress_recorded()
        show_stats()
        
def check(opt):
    global res
    global section_question
    global score
    section_ans=section_question
    if opt==section_ans.loc[qno-1,'Correct_Option']:
        res=1    
    else:
        res=0   
    
def color_button(p):
    if p=='Option A':
        opt1.configure(bg='red')
        opt2.configure(bg='#2eff70')
        opt3.configure(bg='#2eff70')
        opt4.configure(bg='#2eff70')
    elif p=='Option B':
        opt1.configure(bg='#2eff70')
        opt2.configure(bg='red')
        opt3.configure(bg='#2eff70')
        opt4.configure(bg='#2eff70')
    elif p=='Option C':
        opt1.configure(bg='#2eff70')
        opt2.configure(bg='#2eff70')
        opt3.configure(bg='red')
        opt4.configure(bg='#2eff70')
    elif p=='Option D':
        opt1.configure(bg='#2eff70')
        opt2.configure(bg='#2eff70')
        opt3.configure(bg='#2eff70')
        opt4.configure(bg='red') 
    
def score_add():
    global score
    score+=int(res)
    score_label.config(text=f"Score: {score}") 
    
def Progress_recorded():
    global username, score, globalid, user_progress_data, quiz_subjects
    new_row = pd.DataFrame([[username, score, globalid]], columns=["Username", "Score", "Subject"])
    user_progress_data = pd.concat([user_progress_data, new_row], ignore_index=True)
    user_progress_data.to_csv('user_progress.csv', index=False)
    create_piechart(score)
    create_barchart(quiz_subjects,user_progress_data,username)  

def show_stats(): #Showing Statistics frame
    global pie
    Stats_label.config(text=f"Congrats {username} for completing this Quiz!!!")
    Final_score_label.configure(text=f"Score: {score}")
    pie=Image.open('piechart.png')
    pie = pie.resize((400, 400))
    pie = ImageTk.PhotoImage(pie)
    piechart_label.config(image=pie,bg='#E9EDF1')
    show_frame(Stats) 
    
def bargraph_show():
    global bargraph
    bargraph=Image.open('Barchart.png')
    bargraph = bargraph.resize((400, 400))
    bargraph = ImageTk.PhotoImage(bargraph)
    Barchart_Image.config(image=bargraph)
    
def show_graph(pid):
    global username,user_progress_data,Linegraph
    create_linechart(pid,user_progress_data,username)
    Linegraph=Image.open('LineChart.png')
    Linegraph = Linegraph.resize((400, 400))
    Linegraph = ImageTk.PhotoImage(Linegraph)
    Linegraph_Image.config(image=Linegraph)
    
def exit():
    root.destroy()

def restart():
    global qno, score, section_question, res, username, globalid

    # Reset all necessary global variables
    qno = 1
    score = 0
    section_question = None
    res = None
    globalid = None

    # Reset the score label and question display
    score_label.config(text=f"Score: {score}")
    Question_label.config(text="")

    # Reset the options buttons
    opt1.config(bg="#2eff70", text="")
    opt2.config(bg="#2eff70", text="")
    opt3.config(bg="#2eff70", text="")
    opt4.config(bg="#2eff70", text="")

    # Reset the submit button
    submitbtn.config(state=NORMAL)

    show_frame(Declar)


    
user_pass_data=pd.read_csv('users.csv')
questions_data=pd.read_csv('krishna.csv')
user_progress_data=pd.read_csv('user_progress.csv')
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
globalid=NONE
score=0
section_question=NONE
res=NONE

pie=None
bar=None
line=None

fon="vendana"
root = Tk()
root.geometry("900x600")
root.configure(background="#E9EDF1")
root.resizable(0, 0)
root.title('QUIZ')


# Frames
Welcome = Frame(root, background="#E9EDF1")
Login = Frame(root, background="#E9EDF1")
Signup = Frame(root, background="#E9EDF1")
Declar = Frame(root, background="#E9EDF1")
Question = Frame(root, background="#E9EDF1")
Stats=Frame(root,background='#ffffff')
Barchart=Frame(root,background='#ffffff')
SProgress=Frame(root,background="#E9EDF1")
LinegraphFrame=Frame(root,background='#ffffff')

for frame in (Welcome, Signup, Login,Declar,Question,Stats,Barchart,SProgress,LinegraphFrame):
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
    font=(fon,22),
    show="*"
)
signup_password_ent.pack(pady=(13,10),padx=0)

subm_btn=Button(
    Signup,
    text="Submit",
    bg="#5582BE",
    width=20,
    font=(fon,20),
    command=lambda :add_user()
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
    bg="#E9EDF1",
)
login_password_txt.pack(pady=(25,0),padx=(250,0),anchor="w")

login_password_ent=Entry(
    Login,
    width=20,
    font=(fon,22),
    show='*'
)
login_password_ent.pack(pady=(13,10),padx=0)

sub_btn=Button(
    Login,
    text="Submit",
    bg="#5582BE",
    width=20,
    font=(fon,20),
    command=lambda :login_user()
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
btn1 = Button(btnframe1, text=str(quiz_subjects[0]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :(show_frame(Question),Show_Question('General Knowledge')))
btn1.grid(row=0, column=0, padx=20, pady=30)

btn2 = Button(btnframe1, text=str(quiz_subjects[1]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :(show_frame(Question),Show_Question('Science')))
btn2.grid(row=0, column=1, padx=20, pady=30)

btn3 = Button(btnframe1, text=str(quiz_subjects[2]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :(show_frame(Question),Show_Question('Mathematics')))
btn3.grid(row=0, column=2, padx=20, pady=30)

btn4 = Button(btnframe1, text=str(quiz_subjects[3]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :(show_frame(Question),Show_Question('History')))
btn4.grid(row=1, column=0, padx=20, pady=30)

btn5 = Button(btnframe1, text=str(quiz_subjects[4]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :(show_frame(Question),Show_Question('Geography')))
btn5.grid(row=1, column=1, padx=20, pady=30)

btn6 = Button(btnframe1, text=str(quiz_subjects[5]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :(show_frame(Question),Show_Question('Literature')))
btn6.grid(row=1, column=2, padx=20, pady=30)

btn7 = Button(btnframe1, text=str(quiz_subjects[6]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :(show_frame(Question),Show_Question('Technology')))
btn7.grid(row=2, column=0, padx=20, pady=30)

btn8 = Button(btnframe1, text=str(quiz_subjects[7]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :(show_frame(Question),Show_Question('Sports')))
btn8.grid(row=2, column=1, padx=20, pady=30)

btn9 = Button(btnframe1, text=str(quiz_subjects[8]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :(show_frame(Question),Show_Question('Entertainment')))
btn9.grid(row=2, column=2, padx=20, pady=30)

btn10 = Button(btnframe1, text=str(quiz_subjects[9]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :(show_frame(Question),Show_Question('Mythology')))
btn10.grid(row=3, column=0, padx=20, pady=30)

btn11 = Button(btnframe1, text=str(quiz_subjects[10]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :(show_frame(Question),Show_Question('Current Affairs')))
btn11.grid(row=3, column=1, padx=20, pady=30)

btn12 = Button(btnframe1, text=str(quiz_subjects[11]), width=15, font=(fon, 20),bg='#C0EF76',command=lambda :(show_frame(Question),Show_Question('Pop Culture')))
btn12.grid(row=3, column=2, padx=20, pady=30)




#Question 
Question_label=Label(Question,text=str(qno)+"",bg='#E9EDF1',font=(fon,22),wraplength=900,justify="left")
Question_label.pack(anchor='w',padx=(4,6),pady=(10,5))

score_label=Label(Question,text=("Score: "+str(score)),bg="#E9EDF1",font=(fon,18))
score_label.pack(anchor='e')

optionframe=Frame(Question,bg="#E9EDF1")
optionframe.pack(padx=(120,0),anchor='w',pady=(120,0))

opt1=Button(optionframe,text="",font=(fon,18),bg="#2eff70",width=17,command=lambda :(check('Option A'),color_button('Option A')))
opt1.grid(row=0,column=0)

opt2=Button(optionframe,text="",font=(fon,18),bg="#2eff70",width=17,command=lambda :(check('Option B'),color_button('Option B')))
opt2.grid(row=0,column=2,padx=(120,0))

opt3=Button(optionframe,text="",font=(fon,18),bg="#2eff70",width=17,command=lambda :(check('Option C'),color_button('Option C')))
opt3.grid(row=1,column=0,pady=(45,0))

opt4=Button(optionframe,text="",font=(fon,18),bg="#2eff70",width=17,command=lambda :(check('Option D'),color_button('Option D')))
opt4.grid(row=1,column=2,padx=(120,0),pady=(45,0))

submitbtn=Button(Question,text='Submit',font=(fon,20),width=17,bg="#cef522",
                 command=lambda :(score_add(),increase_qno(),show_Questions_forcont()))
submitbtn.pack(anchor="s",pady=(50))


#stats
Stats_label=Label(Stats,text="",font=(fon,34),bg="#ffffff")
Stats_label.pack()

Final_score_label=Label(Stats,text='score',font=(fon,24),bg="#ffffff")
Final_score_label.pack(anchor='w',padx=(45,7),pady=(23,0))

graph_frame=Frame(Stats,bg='#ffffff')
graph_frame.pack()

piechart_label=Label(graph_frame,image=pie)
piechart_label.grid(row=0,column=0,padx=(3,7))

graphbtn_frame=Frame(graph_frame,bg="#ffffff")
graphbtn_frame.grid(row=0,column=1)

barbtn=Button(graphbtn_frame,text='View your highest in each subject',font=(fon,14),command=lambda :(bargraph_show(),show_frame(Barchart)))
barbtn.grid(row=0,column=0,padx=(7,9),pady=(0,10))

linebtn=Button(graphbtn_frame,text='View your progress in each subject',font=(fon,14),command=lambda :(show_frame(SProgress)))
linebtn.grid(row=1,column=0,padx=(7,9),pady=(5,8))

restartbtn=Button(graphbtn_frame,text='Back',font=(fon,14),command=lambda :restart())
restartbtn.grid(row=2,column=0,padx=(7,9),pady=(5,8))

exitbtn=Button(graphbtn_frame,text='exit',font=(fon,14),command=lambda: exit())
exitbtn.grid(row=3,column=0,padx=(7,9),pady=(5,8))



#Barchart
bargraph=None
Barchart_Image=Label(Barchart,image=bargraph)
Barchart_Image.pack()

backbtn=Button(Barchart,bg='blue',text="Back",command=lambda :show_frame(Stats))
backbtn.pack(anchor='s')

#SProgress
Pbtnframe = Frame(SProgress, bg="#E9EDF1")
Pbtnframe.pack(pady=(70, 0))

Pbtn1 = Button(Pbtnframe, text=str(quiz_subjects[0]), width=15, font=(fon, 20),bg='#C0EF76'
               ,command=lambda :(show_frame(LinegraphFrame),show_graph(quiz_subjects[0])))
Pbtn1.grid(row=0, column=0, padx=20, pady=30)

Pbtn2 = Button(Pbtnframe, text=str(quiz_subjects[1]), width=15, font=(fon, 20),bg='#C0EF76'
               ,command=lambda :(show_frame(LinegraphFrame),show_graph(quiz_subjects[1])))
Pbtn2.grid(row=0, column=1, padx=20, pady=30)

Pbtn3 = Button(Pbtnframe, text=str(quiz_subjects[2]), width=15, font=(fon, 20),bg='#C0EF76'
               ,command=lambda :(show_frame(LinegraphFrame),show_graph(quiz_subjects[2])))
Pbtn3.grid(row=0, column=2, padx=20, pady=30)

Pbtn4 = Button(Pbtnframe, text=str(quiz_subjects[3]), width=15, font=(fon, 20),bg='#C0EF76'
               ,command=lambda :(show_frame(LinegraphFrame),show_graph(quiz_subjects[3])))
Pbtn4.grid(row=1, column=0, padx=20, pady=30)

Pbtn5 = Button(Pbtnframe, text=str(quiz_subjects[4]), width=15, font=(fon, 20),bg='#C0EF76'
               ,command=lambda :(show_frame(LinegraphFrame),show_graph(quiz_subjects[4])))
Pbtn5.grid(row=1, column=1, padx=20, pady=30)

Pbtn6 = Button(Pbtnframe, text=str(quiz_subjects[5]), width=15, font=(fon, 20),bg='#C0EF76'
               ,command=lambda :(show_frame(LinegraphFrame),show_graph(quiz_subjects[5])))
Pbtn6.grid(row=1, column=2, padx=20, pady=30)

Pbtn7 = Button(Pbtnframe, text=str(quiz_subjects[6]), width=15, font=(fon, 20),bg='#C0EF76'
               ,command=lambda :(show_frame(LinegraphFrame),show_graph(quiz_subjects[6])))
Pbtn7.grid(row=2, column=0, padx=20, pady=30)

Pbtn8 = Button(Pbtnframe, text=str(quiz_subjects[7]), width=15, font=(fon, 20),bg='#C0EF76'
               ,command=lambda :(show_frame(LinegraphFrame),show_graph(quiz_subjects[7])))
Pbtn8.grid(row=2, column=1, padx=20, pady=30)

Pbtn9 = Button(Pbtnframe, text=str(quiz_subjects[8]), width=15, font=(fon, 20),bg='#C0EF76'
               ,command=lambda :(show_frame(LinegraphFrame),show_graph(quiz_subjects[8])))
Pbtn9.grid(row=2, column=2, padx=20, pady=30)

Pbtn10 = Button(Pbtnframe, text=str(quiz_subjects[9]), width=15, font=(fon, 20),bg='#C0EF76'
                ,command=lambda :(show_frame(LinegraphFrame),show_graph(quiz_subjects[9])))
Pbtn10.grid(row=3, column=0, padx=20, pady=30)

Pbtn11 = Button(Pbtnframe, text=str(quiz_subjects[10]), width=15, font=(fon, 20),bg='#C0EF76'
                ,command=lambda :(show_frame(LinegraphFrame),show_graph(quiz_subjects[10])))
Pbtn11.grid(row=3, column=1, padx=20, pady=30)

Pbtn12 = Button(Pbtnframe, text=str(quiz_subjects[11]), width=15, font=(fon, 20),bg='#C0EF76'
                ,command=lambda :(show_frame(LinegraphFrame),show_graph(quiz_subjects[11])))
Pbtn12.grid(row=3, column=2, padx=20, pady=30)

Pbackbtn=Button(SProgress,bg='blue',text="Back"
                ,command=lambda :show_frame(Stats))
Pbackbtn.pack()



#LinegraphFrame
Linegraph=None
Linegraph_Image=Label(LinegraphFrame,image=Linegraph)
Linegraph_Image.grid(row=0,column=0)

Lbackbtn=Button(LinegraphFrame,bg='blue',text="Back",command=lambda :show_frame(SProgress))
Lbackbtn.grid(row=1,column=0)


root.mainloop()