from tkinter import 
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    priority = priority_var.get()
    if task != "":
        lb.insert(END, f"{task} ({priority})")
        my_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

def deleteTask():
    try:
        index = lb.curselection()[0]
        lb.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def updateTask():
    try:
        index = lb.curselection()[0]
        task = my_entry.get()
        priority = priority_var.get()
        if task != "":
            lb.delete(index)
            lb.insert(index, f"{task} ({priority})")
            my_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "Please enter some task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def searchTask():
    search_term = search_entry.get().lower()
    lb.delete(0, END)
    for task in tasks:
        if search_term in task.lower():
            lb.insert(END, task)

ws = Tk()
ws.geometry('600x500+500+200')
ws.title('Enhanced To-Do List')
ws.config(bg="#ffe6e6")
ws.resizable(width=False, height=False)

tasks = []

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=50,
    height=10,
    bd=0,
    font=("Helvetica", 12),
    selectbackground="#ff9999"
)
lb.pack(side=LEFT, fill=BOTH)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=("Helvetica", 24),
    bg="#ffe6e6"
)
my_entry.pack(pady=10)

priority_var = StringVar(value="Medium")
priority_menu = OptionMenu(ws, priority_var, "High", "Medium", "Low")
priority_menu.pack(pady=10)

button_frame = Frame(ws)
button_frame.pack(pady=10)

addTask_btn = Button(
    button_frame,
    text="Add Task",
    font=("Helvetica", 14),
    bg="#ff6666",
    fg="white",
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text="Delete Task",
    font=("Helvetica", 14),
    bg="#ff3333",
    fg="white",
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

updateTask_btn = Button(
    button_frame,
    text="Update Task",
    font=("Helvetica", 14),
    bg="#ff9999",
    fg="white",
    padx=20,
    pady=10,
    command=updateTask
)
updateTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

search_entry = Entry(
    ws,
    font=("Helvetica", 14),
    bg="#ffe6e6"
)
search_entry.pack(pady=10)

search_btn = Button(
    ws,
    text="Search Task",
    font=("Helvetica", 14),
    bg="#ff9999",
    fg="white",
    command=searchTask
)
search_btn.pack(pady=10)

ws.mainloop()