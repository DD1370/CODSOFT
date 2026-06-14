import tkinter as tk
from tkinter import messagebox,simpledialog
import json

class BeginNow:
    def __init__(self,root):
        self.root = root
        self.root.title("BeginNow") 
        self.root.geometry("600x450")
        self.root.resizable(False,False)
        self.root.configure(bg="#F4F1EA")

        self.tasks = self.load_tasks()
        self.setup_ui()
        self.refresh_listbox()
        
    def setup_ui(self):
        # title label
        title_label = tk.Label(
            self.root,
            text="✨BeginNow✨\nOrganise your day!",
            font=("Arial",22,"bold"),
            bg="#F4F1EA",
            fg= "#2C3E2B"
        )
        title_label.pack(pady=10)

        # text box frame
        input_frame= tk.Frame(
            self.root,
            bg="#E6E1D5"
        )
        input_frame.pack(pady=10)

        # text box
        self.task_entry =tk.Entry (
            input_frame,
            font=("Arial",12),
            bg="#FFFFFF",
            fg="#2C3E2B",
            insertbackground="#2C3E2B",
            width=40)
        self.task_entry.pack(side="left",padx=(10,10))
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        #add task button
        add_button = tk.Button(
            input_frame,
            text="Add task ➕",
            font=("Arial",11,"bold"),
            bg="#A3B18A",                                    #<---------
            fg="#2C3E2B",
            padx=10,
            command=self.add_task
        )
        add_button.pack(side="left")

        # task list frame
        list_frame= tk.Frame(
            self.root,
            bg="#E6E1D5",
                                                                                                                    #<------
        )
        list_frame.pack(pady=10,expand=True)

        # task list box
        self.task_listbox= tk.Listbox(
            list_frame,
            font=("Arial",12),
            width= 45,
            height= 10,
            bg="#FFFFFF",
            fg="#2C3E2B",
            selectbackground="#A3B18A",
            activestyle=None                                                     #<------
        )
        self.task_listbox.pack(side="left", fill="both", expand= True)

        # Scroll bar
        scroll_bar= tk.Scrollbar(list_frame)
        scroll_bar.pack(side="right",fill="y")
        self.task_listbox.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.task_listbox.yview)

        #status label
        self.info_label = tk.Label(
            self.root,
            text="",
            font=("Arial",11,"bold"),
            bg="#F4F1EA",
            fg="#2C3E2B"
        )
        self.info_label.pack(pady=5)

        # Action buttons frame
        button_frame= tk.Frame(self.root,bg="#F4F1EA")
        button_frame.pack(pady=(10,10))

        edit_button = tk.Button(
            button_frame,
            text="Edit Task ✏️",
            font=("Arial",11,"bold"),
            bg="#D8C3A5",
            fg="#2C3E2B",
            padx=10,
            command=self.edit_task
        )
        edit_button.pack(side="left", padx=5)

        # mark as done button
        mark_done_button= tk.Button(
            button_frame,
            text="Track Status (✅|🔲)",
            font=("Arial",11,"bold"),
            bg="#A3B18A",
            fg="#2C3E2B",
            padx=10,
            command=self.mark_done
        )
        mark_done_button.pack(side="left",padx=5)
        

        #delete task button
        delete_button= tk.Button(
            button_frame,
            text="Delete Task 🗑️",
            font=("Arial",11,"bold"),
            bg="#E07A5F",
            fg="#2C3E2B",
            padx=10,
            command=self.delete_task
        )
        delete_button.pack(side="left",padx=5)

        
        # clear all buuton
        clear_button= tk.Button(
            button_frame,
            text="Clear All 🧹",
            font=("Arial",11,"bold"),
            bg="#B8B7B3",
            fg= "#2C3E2B",
            padx=10,
            command=self.clear_all
        )
        clear_button.pack(side="left",padx=5)
    
    def refresh_listbox(self):
        self.task_listbox.delete(0,tk.END)
        for index,task in enumerate(self.tasks,start=1):
            status= "✅" if task["done"] else "🔲"
            display_text=f"{status} {index}. {task['task']}"
            self.task_listbox.insert(tk.END,display_text)

    def add_task(self):
        task_text=self.task_entry.get().strip()
        
        if not task_text:
            self.info_label.config(text="Please enter a task first.")
            return
        self.tasks.append({"task":task_text,"done": False})
        self.save_tasks()
        self.task_entry.delete(0,tk.END)
        self.info_label.config(text=f"Task '{task_text}' added!")
        self.refresh_listbox()

    def get_selected_index(self):
        selection=self.task_listbox.curselection()
        if not selection:
            messagebox.showinfo("BeginNow","No Selection,Please Select a task first.")
            return None                                                         # <-------------------------
        return selection[0]
    
    def mark_done(self):
        index = self.get_selected_index()
        if index is None:
            return
        self.tasks[index]["done"] = not self.tasks[index]["done"]
        self.save_tasks()
        if self.tasks[index]["done"]:
            self.info_label.config(text="Task marked as done!")
        else:
            self.info_label.config(text="Task marked as pending!")
        self.refresh_listbox()
    def edit_task(self):
            index = self.get_selected_index()
            if index is None:
                return
            current_task = self.tasks[index]["task"]
            new_task = simpledialog.askstring("Edit Task","Update your task:",initialvalue=current_task)
            if new_task and new_task.strip():
                self.tasks[index]["task"] = new_task.strip()
                self.save_tasks()
                self.refresh_listbox()
                self.info_label.config(text="Task updated successfully!")

    def delete_task(self):
        index= self.get_selected_index()
        if index is None:
            return
        removed =self.tasks.pop(index) 
        self.save_tasks() 
        self.info_label.config(text=f"Deleted task: {removed['task']}")  
        self.refresh_listbox()

    def clear_all(self):
        if not self.tasks:
            self.info_label.config(text ="No tasks to clear.")
            return
        if messagebox.askyesno("Clear All"," Are you sure you want to delete all tasks?"):
            self.tasks.clear()
            self.save_tasks()
            self.refresh_listbox()
            self.info_label.config(text="All tasks cleared!")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                return json.load(file)
        except FileNotFoundError: 
            return []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = BeginNow(root)    
    root.mainloop()