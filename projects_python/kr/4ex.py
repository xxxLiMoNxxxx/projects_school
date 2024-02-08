from cgitb import text
import tkinter as tk
from turtle import color
from tkinter import messagebox

#функція
def numbers():
    entryget = int(entry.get())
    if (entryget > 0):
        messagebox.showinfo("Інформація!", "Ваше число більше за 0")
    elif(entryget < 0):
        messagebox.showinfo("Інформація!", "Ваше число менше за 0")
    else:
        messagebox.showinfo("Інформація!", "Ваше число 0")
        

root = tk.Tk()
#налаштування
root.geometry("1920x1080")
root.minsize(50, 50)
root.resizable(False, False)
root.title("Застосунок")
#текста та все таке
entry = tk.Entry(root)
button1 = tk.Button(root, text="ок", command=numbers)

#cпавн
entry.pack()
button1.pack()

root.mainloop()