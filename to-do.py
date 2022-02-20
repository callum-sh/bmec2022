from importlib.machinery import WindowsRegistryFinder
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
 
app = tk.Tk()

app.title('BMEC2022: Power Ranger To-Do Demo')
fontStyle = tkFont.Font(family="Open Sans", size = 30)


canvas = Canvas(app, bg="white", height=1000, width=1000)
canvas.create_text(350, 30, text="Task", fill="black", font=fontStyle)
canvas.pack()


NUM_TASKS = 14
i = 0
num = 0

tsk = StringVar()
desc = StringVar()

app.geometry("900x500")
app.resizable(0, 0)

tasks = {0:"Wash, brush teeth, get dressed", 
1:"Prepare and eat breakfast", 
2:"Have a conversation over coffee", 
3:"Discuss the newspaper, try a craft project, reminisce about old photos", 
4:"Take a break, have some quiet time", 
5:"Do some chores together", 
6:"Take a walk, play an active game", 
7:"Prepare and eat lunch, read mail, wash dishes", 
8:"Listen to music, do crossword puzzles, watch TV", 
9:"Do some gardening, take a walk, visit a friend", 
10:"Take a short break or nap", 
11:"Prepare and eat dinner, clean up the kitchen", 
12:"Reminisce over coffee and dessert", 
13:"Play cards, watch a movie, give a massage",
14:"Take a bath, get ready for bed, read a book"}

tasks_second_info = {0:"Location: bathroom", 
1:"Location: kitchen", 
2:"Location: kitchen", 
3:"Location: living room", 
4:"Location: living room", 
5:"Location: living room", 
6:"Location: garden", 
7:"Location: kitchen", 
8:"Location: living room", 
9:"Location: garden", 
10:"Location: bedroom", 
11:"Location: kitchen", 
12:"Location: dining room", 
13:"Location: living room",
14:"Location: bathroom/bedroom"}

def onButtonPush():
    global i
    i = i + 1
    global num
    num = i % NUM_TASKS

    task_box = Canvas(app, bg="#add8e6")
    task_box.create_text(250, 80, text=tasks[num], fill="black", font=fontStyle)
    task_box.place(x=320, y=60, height=270, width=570)

    loc = Canvas(app, bg='#ffcccb')
    loc.create_text(250, 80, text=tasks_second_info[num], fill="black", font=fontStyle)
    loc.place(x=320, y=340, height=150, width=570)

temp = Canvas(app, bg="#add8e6")
temp.create_text(250, 80, text="Press 'Next Task' to Start", fill="black", font=fontStyle)
temp.place(x=320, y=60, height=270, width=570)

loc_temp = Canvas(app, bg='#ffcccb')
loc_temp.create_text(250, 80, text="Location Info", fill="black", font=fontStyle)
loc_temp.place(x=320, y=340, height=150, width=570)

task_label_txt = StringVar()
task_label_txt.set("Task")

# task_label = tk.Message(app, textvariable=task_label_txt, font=fontStyle, width=400)
# task_label.place(x=330, y=10)

button = tk.Button(app, text="Next Task", font=fontStyle, highlightbackground="#90ee90", fg="Black", highlightthickness=200, command=onButtonPush)
button.place(x=10, y=10, width=300, height=480)

# label = tk.Message(app, textvariable=tsk, font=fontStyle, width=400)
# label.place(x=350, y=70)



app.mainloop()