'''
Application developed by Mohammed Javeed
To-Do list managing application develped in Python
GUI built using tkinter and ttkbootstrap
Uses tkinter.messagebox for displaying messages
Uses "sandstone" theme
Data stored in SQLite
'''

# Importing the required modules
import tkinter as tk
import ttkbootstrap as ttk
import sqlite3
import datetime
from datetime import date
from tkcalendar import DateEntry
from tkinter import messagebox
from ttkbootstrap import Style


# Creating the database connection and cursor
conn = sqlite3.connect("todo.db")
c = conn.cursor()

# Creating the table if it does not exist
c.execute("""CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    description TEXT,
    due_date TEXT,
    priority TEXT,
    status TEXT
)""")
conn.commit()

# Creating the window window
window = tk.Tk()
window.title("To-Do List Manager")
window.geometry("1000x500")
# Set a theme
style = Style(theme="sandstone")

# Creating the notebook widget to have tab view
notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

# Creating the frames for each tab
frame_tasks = ttk.Frame(notebook)
frame_complete = ttk.Frame(notebook)

frame_task_tree = ttk.Frame(frame_tasks)
frame_entry= ttk.Frame(frame_tasks)
frame_buttons = ttk.Frame(frame_tasks)
frame_task_tree.pack(anchor="center", side='top', fill="both", expand=True)
frame_entry.pack(anchor="center", expand=False)
frame_buttons.pack(anchor="center", expand=False)

# Adding the frames to the notebook
notebook.add(frame_tasks, text="Tasks in progress")
notebook.add(frame_complete, text="Completed")

# Creating the treeview widgets for each tab
tree_tasks = ttk.Treeview(frame_task_tree, columns=("Description", "Due Date", "Priority"), show="headings")
tree_complete = ttk.Treeview(frame_complete, columns=("Description", "Due Date", "Priority"), show="headings")

# Configuring the treeview columns
tree_tasks.column("Description", width=300, anchor="w")
tree_tasks.column("Due Date", width=100, anchor="center")
tree_tasks.column("Priority", width=100, anchor="center")

tree_complete.column("Description", width=300, anchor="w")
tree_complete.column("Due Date", width=100, anchor="center")
tree_complete.column("Priority", width=100, anchor="center")

# Configuring the treeview headings
tree_tasks.heading("Description", text="Description")
tree_tasks.heading("Due Date", text="Due Date")
tree_tasks.heading("Priority", text="Priority")

tree_complete.heading("Description", text="Description")
tree_complete.heading("Due Date", text="Due Date")
tree_complete.heading("Priority", text="Priority")

# Creating the scrollbar widgets for each tab
scroll1 = ttk.Scrollbar(frame_task_tree, orient="vertical", command=tree_tasks.yview)
scroll2 = ttk.Scrollbar(frame_complete, orient="vertical", command=tree_complete.yview)

# Configuring the treeview scrollbars
tree_tasks.configure(yscrollcommand=scroll1.set)
tree_complete.configure(yscrollcommand=scroll2.set)
style.configure("Treeview.Heading", font=('', 10, "bold"), background="#EAEAEA")
style.configure("Treeview", font=("calibri", 12), background="#F8F8FF", rowheight=20)

# Packing the treeview and scrollbar widgets
tree_tasks.pack(side="left", fill="both", expand=True)
scroll1.pack(side="right", fill="y")

tree_complete.pack(side="left", fill="both", expand=True)
scroll2.pack(side="right", fill="y")


# Creating the label and entry widgets for the input boxes
label_desc = ttk.Label(frame_entry, text="Description:")
label_duedate = ttk.Label(frame_entry, text="Due Date:")
label_priority = ttk.Label(frame_entry, text="Priority:")

entry_desc = ttk.Entry(frame_entry, width=60)
entry_duedate = ttk.DateEntry(frame_entry)
entry_priority = ttk.Combobox(frame_entry, values=["High", "Medium", "Low"])

# Packing the label and entry widgets
label_desc.pack(side="left", padx=10, pady=30)
entry_desc.pack(side="left", padx=10, pady=30)
label_duedate.pack(side="left", padx=10, pady=30)
entry_duedate.pack(side="left", padx=10, pady=30)
label_priority.pack(side="left", padx=10, pady=30)
entry_priority.pack(side="left", padx=10, pady=30)

# Creating the button widgets
button_add = ttk.Button(frame_buttons, text="Add Task")
button_complete = ttk.Button(frame_buttons, text="Complete Task")
button_delete = ttk.Button(frame_buttons, text="Delete Task")
button_exit = ttk.Button(frame_buttons, text="Exit")

# Packing the button widgets
button_add.pack(side="left", padx=10, pady=20)
button_complete.pack(side="left", padx=10, pady=20)
button_delete.pack(side="left", padx=10, pady=20)
button_exit.pack(side="left", padx=10, pady=20)

# Defining the function to add a task to the database and the treeview
def add_task():
    # Getting the input values
    description = entry_desc.get()
    due_date = entry_duedate.entry.get()
    due_date = datetime.datetime.strptime(due_date,'%m/%d/%Y').strftime("%d-%b-%Y")
    priority = entry_priority.get()

    # Checking if the input values are valid
    if description and due_date and priority:
        # Inserting the task into the database
        c.execute("INSERT INTO tasks (description, due_date, priority, status) VALUES (?, ?, ?, ?)", (description, due_date, priority, "In progress"))
        conn.commit()

        # Getting the id of the inserted task
        id = c.lastrowid

        # Inserting the task into the treeview
        tree_tasks.insert("", "end", iid=id, values=(description, due_date, priority))

        # Clearing the input boxes
        entry_desc.delete(0, "end")
        entry_priority.set("")

        # Showing a success message
        tk.messagebox.showinfo("Success", "Task added successfully!")
    else:
        # Showing an error message
        tk.messagebox.showerror("Error", "Please enter valid values for all fields!")

# Defining the function to mark a task as complete and move it to the other treeview
def complete_task():
    # Getting the selected item in the treeview
    selected = tree_tasks.selection()

    # Checking if an item is selected
    if selected:
        # Looping through the selected items
        for item in selected:
            # Getting the values of the item
            values = tree_tasks.item(item, "values")

            # Updating the status of the task in the database
            c.execute("UPDATE tasks SET status = ? WHERE id = ?", ("Completed", item))
            conn.commit()

            # Deleting the item from the treeview
            tree_tasks.delete(item)

            # Inserting the item into the other treeview
            tree_complete.insert("", "end", iid=item, values=values)

        # Showing a success message
        tk.messagebox.showinfo("Success", "Task(s) marked as complete!")
    else:
        # Showing an error message
        tk.messagebox.showerror("Error", "Please select a task to mark as complete!")

# Defining the function to delete a task from the database and the treeview
def delete_task():
    # Getting the selected item in the treeview
    selected = tree_tasks.selection()

    # Checking if an item is selected
    if selected:
        # Looping through the selected items
        for item in selected:
            # Deleting the task from the database
            c.execute("DELETE FROM tasks WHERE id = ?", (item,))
            conn.commit()

            # Deleting the item from the treeview
            tree_tasks.delete(item)

        # Showing a success message
        tk.messagebox.showinfo("Success", "Task(s) deleted successfully!")
    else:
        # Showing an error message
        tk.messagebox.showerror("Error", "Please select a task to delete!")

# Defining the function to exit the application
def exit():
    # Asking for confirmation
    answer = tk.messagebox.askyesno("Exit", "Are you sure you want to exit?")

    # Checking the answer
    if answer:
        # Closing the database connection
        conn.close()

        # Destroying the window window
        window.destroy()

# Binding the button widgets to the corresponding functions
button_add.configure(command=add_task)
button_complete.configure(command=complete_task)
button_delete.configure(command=delete_task)
button_exit.configure(command=exit)

# Defining the function to load the tasks from the database to the treeviews
def load_tasks():
    # Getting all the tasks from the database
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()

    # Looping through the tasks
    for task in tasks:
        # Getting the task details
        id, description, due_date, priority, status = task

        # Checking the status of the task
        if status == "In progress":
            # Inserting the task into the first treeview
            tree_tasks.insert("", "end", iid=id, values=(description, due_date, priority))
        else:
            # Inserting the task into the second treeview
            tree_complete.insert("", "end", iid=id, values=(description, due_date, priority))

# Calling the function to load the tasks
load_tasks()

# Starting the main loop
window.mainloop()
