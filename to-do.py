import tkinter as tk
from tkinter import StringVar, messagebox
from tkinter import *
import tkinter.font as tkFont
from turtle import color
import platform

app = tk.Tk()

app.title('BMEC2022: Power Ranger To-Do Demo')

NUM_TASKS = 14
i = 0
num = 0

tsk = StringVar()
desc = StringVar()

app.geometry("900x500")
fontStyle = tkFont.Font(family="Open Sans", size = 30)

tsk.set("Click 'Finish Task' to Start")

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


def onButtonPush():
    global i
    i = i + 1
    global num
    num = i % NUM_TASKS
    tsk.set(tasks[num])

task_label_txt = StringVar()
task_label_txt.set("Task")

task_label = tk.Message(app, textvariable=task_label_txt, font=fontStyle, width=400)
task_label.config(borderwidth=10, fg='white')
task_label.place(x=320, y=10)


button = tk.Button(app, text="Finished Task", highlightbackground="#90ee90", fg="Black", highlightthickness=200, command=onButtonPush)
button.place(x=10, y=10, width=300, height=480)

label = tk.Message(app, textvariable=tsk, font=fontStyle, width=400)
label.config(borderwidth=10, fg='black', background='#add8e6')
label.place(x=350, y=70)

app.mainloop()