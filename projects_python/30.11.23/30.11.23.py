import tkinter as tk
from tkinter import Button, Entry, messagebox

root = tk.Tk()

def show_message():
    user_input = entry.get()
    message = f"Привіт, {user_input}!"
    if user_input:
        messagebox.showinfo("Повідомлення", message)
    else:
        messagebox.showerror("Помилка", "Ви не ввели своє ім'я")

root.geometry("800x600")
root.minsize(50, 50)
root.resizable(False, False)
root.title("Застосунок")

label = tk.Label(root, text="Введіть своє ім'я", font="Arial 18", foreground="red")
entry = tk.Entry(root)
button = tk.Button(root, text="ок", command=show_message)

label.pack()
entry.pack()
button.pack()

root.mainloop()