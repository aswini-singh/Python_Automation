import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        action_history.append(("add", task))
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a selected task
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        removed_task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        action_history.append(("remove", removed_task))
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Function to view tasks
def view_tasks():
    tasks = listbox.get(0, tk.END)
    if tasks:
        tasks_str = "\n".join(tasks)
        messagebox.showinfo("To-Do List", "Tasks:\n" + tasks_str)
    else:
        messagebox.showinfo("To-Do List", "No tasks in the list.")

# Function to edit a selected task
def edit_task():
    try:
        selected_task_index = listbox.curselection()[0]
        current_task = listbox.get(selected_task_index)
        new_task = entry.get()
        if new_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, new_task)
            action_history.append(("edit", (current_task, new_task)))
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

# Function to undo the last action
def undo_action():
    if action_history:
        action_type, action_data = action_history.pop()
        if action_type == "add":
            # Undo an add action by removing the last task
            last_task = action_data
            listbox.delete(tk.END)
        elif action_type == "remove":
            # Undo a remove action by adding the removed task back
            removed_task = action_data
            listbox.insert(tk.END, removed_task)
        elif action_type == "edit":
            # Undo an edit action by reverting to the previous task
            current_task, previous_task = action_data
            selected_task_index = listbox.get(0, tk.END).index(current_task)
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, previous_task)
    else:
        messagebox.showinfo("Info", "No actions to undo.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Entry widget for adding tasks
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Add task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Remove task button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Edit task button
edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack()

# View tasks button
view_button = tk.Button(root, text="View Tasks", command=view_tasks)
view_button.pack()

# Undo button
undo_button = tk.Button(root, text="Undo", command=undo_action)
undo_button.pack()

# Listbox to display tasks
listbox = tk.Listbox(root, width=40)
listbox.pack()

# Initialize the action history list
action_history = []

# Function to center the window on the screen
def center_window(width=300, height=200):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

# Center the main window
center_window(400, 400)

# Start the Tkinter main loop
root.mainloop()
