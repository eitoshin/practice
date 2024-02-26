import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Task:
    def __init__(self, description, due_date, details=""):
        self.description = description
        self.due_date = due_date
        self.details = details
        self.completed = False

    def complete(self):
        self.completed = True

class ToDoApp:
    def __init__(self, master):
        self.master = master
        master.title("ToDo App")

        self.tasks = []

        self.left_frame = tk.Frame(master)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.right_frame = tk.Frame(master)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.label = tk.Label(self.left_frame, text="ToDo List")
        self.label.pack()

        self.task_listbox = tk.Listbox(self.left_frame, selectmode=tk.SINGLE)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)
        self.task_listbox.bind("<<ListboxSelect>>", self.display_task_details)

        self.display_tasks()

        self.description_label = tk.Label(self.right_frame, text="Task Description:")
        self.description_label.pack()

        self.task_entry = tk.Entry(self.right_frame)
        self.task_entry.pack()

        self.date_label = tk.Label(self.right_frame, text="Due Date (YYYY-MM-DD):")
        self.date_label.pack()

        self.default_date = datetime.today().strftime('%Y-%m-%d')
        self.date_entry = tk.Entry(self.right_frame)
        self.date_entry.insert(tk.END, self.default_date)
        self.date_entry.pack()

        self.task_detail_label = tk.Label(self.right_frame, text="Task Details:")
        self.task_detail_label.pack()

        self.task_detail_text = tk.Text(self.right_frame, height=5, width=30)
        self.task_detail_text.pack()

        self.add_button = tk.Button(self.right_frame, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(self.right_frame, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

    def add_task(self):
        description = self.task_entry.get()
        date_str = self.date_entry.get()
        details = self.task_detail_text.get("1.0", tk.END).strip()
        try:
            year, month, day = map(int, date_str.split("-"))
            due_date = datetime(year, month, day)
            task = Task(description, due_date, details)
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task.description)
            self.task_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(tk.END, self.default_date)
            self.task_detail_text.delete(1.0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks[index]
            task.complete()
            self.task_listbox.delete(index)
            self.clear_task_details()  # Ç±Ç±Ç≈ÉGÉâÅ[Ç™î≠ê∂
        except IndexError:
            messagebox.showerror("Error", "Please select a task to complete.")

    def clear_task_details(self):
        self.task_detail_text.delete(1.0, tk.END)

    def display_tasks(self):
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task.description)

    def display_task_details(self, event):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks[index]
            self.task_detail_text.delete(1.0, tk.END)
            self.task_detail_text.insert(tk.END, task.details)
        except IndexError:
            pass

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
