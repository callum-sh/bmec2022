import tkinter as tk
from tkinter import StringVar, messagebox
import tkinter.font as tkFont

app = tk.Tk()

NUM_TASKS = 14
i = 0
num = 0

app.geometry("900x500")

tsk = StringVar()

desc = StringVar()

def t0():
    return "Wash, brush teeth, get dressed"

def t1():
    return "Prepare and eat breakfast"

def t2():
    return "Have a conversation over coffee"

def t3():
    return "Discuss the newspaper, try a craft project, reminisce about old photos"

def t4():
    return "Take a break, have some quiet time"

def t5():
    return "Do some chores together"

def t6():
    return "Take a walk, play an active game"

def t7():
    return "Prepare and eat lunch, read mail, wash dishes"

def t8():
    return "Listen to music, do crossword puzzles, watch TV"

def t9():
    return "Do some gardening, take a walk, visit a friend"

def t10():
    return "Take a short break or nap"

def t11():
    return "Prepare and eat dinner, clean up the kitchen"

def t12():
    return "Reminisce over coffee and dessert"

def t13():
    return "Play cards, watch a movie, give a massage"

def t14():
    return "Take a bath, get ready for bed, read a book"

tasks = {0:t0, 1:t1, 2:t2, 3:t3, 4:t4, 5:t5, 6:t6, 7:t7, 8:t8, 9:t9, 10:t10, 11:t11, 12:t12, 13:t13, 14:t14}


def onButtonPush():
    global i
    i = i + 1
    global num
    num = i % NUM_TASKS
    tsk.set(tasks[num]())

button = tk.Button(app, text="Finished Task", command=onButtonPush, width=30, height=29)
button.place(x=10, y=10)

fontStyle = tkFont.Font(family="Open Sans", size = 30)

label = tk.Message(app, textvariable=tsk, font=fontStyle, width=400)
label.place(x=400, y=150)

app.mainloop()