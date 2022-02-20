from importlib.machinery import WindowsRegistryFinder
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
 
# init values for task count (i), task index (num), and the number of tasks (NUM_TASKS)
NUM_TASKS = 18
i = 0
num = 0

# start GUI application 
app = tk.Tk()

# housekeeping
fontStyle = tkFont.Font(family="Open Sans", size = 30)

# set size of screen and dont let it change
app.geometry("900x500")
app.resizable(0, 0)

# title 
app.title('BMEC2022: Power Ranger To-Do Demo')

# make background white
canvas = Canvas(app, bg="white", height=1000, width=1000)
canvas.create_text(350, 30, text="Task", fill="black", font=fontStyle)
canvas.pack()

# Data Struct to store each task as follows: (task, location)
tasks = {0: ("MORNING TASKS", "Time: 8:00am"),
1:("Wash, brush teeth, get dressed", "Location: bathroom"),
2: ("Prepare and eat breakfast", "Location: kitchen"), 
3: ("Have a conversation over coffee", "Location: kitchen"), 
4: ("Discuss the newspaper, try a craft project, reminisce about old photos",  "Location: living room"),
5: ("Take a break, have some quiet time", "Location: living room"), 
6: ("Do some chores together", "Location: living room"),
7: ("Take a walk, play an active game", "Location: garden"),
8: ("LUNCH TASKS", "Time: 12:00pm"),
9: ("Prepare and eat lunch, read mail, wash dishes", "Location: kitchen"),
10: ("Listen to music, do crossword puzzles, watch TV","Location: living room"), 
11: ("Do some gardening, take a walk, visit a friend", "Location: garden"),
12: ("Take a short break or nap", "Location: bedroom"),
13: ("DINNER TASKS", "Time: 6:00pm"),
14: ("Prepare and eat dinner, clean up the kitchen", "Location: kitchen"),
15: ("Reminisce over coffee and dessert", "Location: dining room"), 
16: ("Play cards, watch a movie, give a massage", "Location: living room"),
17: ("Take a bath, get ready for bed, read a book", "Location: bathroom/bedroom")}

'''
Update the shown task on button press
'''
def onButtonPush():
    # update the index of the task
    global i
    i = i + 1
    global num
    num = i % NUM_TASKS
    # display the new task
    task_box = Canvas(app, bg="#add8e6")
    task_box.create_text(290, 100, text=tasks[num][0], fill="black", font=fontStyle, width=500)
    task_box.place(x=320, y=60, height=270, width=570)
    # display the new location/time
    loc = Canvas(app, bg='#ffcccb')
    loc.create_text(250, 80, text=tasks[num][1], fill="black", font=fontStyle)
    loc.place(x=320, y=340, height=150, width=570)

# set up starting task instructions
temp = Canvas(app, bg="#add8e6")
temp.create_text(250, 80, text="Press 'Next Task' to Start", fill="black", font=fontStyle)
temp.place(x=320, y=60, height=270, width=570)

# set up starting location instructions
loc_temp = Canvas(app, bg='#ffcccb')
loc_temp.create_text(250, 80, text="Location Info", anchor=N, fill="black", font=fontStyle, width=500)
loc_temp.place(x=320, y=340, height=150, width=570)

# task label
task_label_txt = StringVar()
task_label_txt.set("Task")

# make 'Next Task' button
button = tk.Button(app, text="Next Task", font=fontStyle, highlightbackground="#90ee90", fg="Black", highlightthickness=200, command=onButtonPush)
button.place(x=10, y=10, width=300, height=480)

# start application
app.mainloop()