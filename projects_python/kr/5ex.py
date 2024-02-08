from cgitb import text
import tkinter as tk
from turtle import color
from tkinter import messagebox

#функція
def numbers():
    entryget = int(entry.get())
    if (entryget >= 20000):
        messagebox.showinfo("Інформація!", "Ви купили автомобіль!")
        while(True):
            entryget -= 20000
            label_money.config(text=(f"Ваші гроші: {entryget}"))
            break
    elif(entryget < 20000):
        messagebox.showerror("Помилка!", "Вам не хватає грошей!")
        while(True):
            label_money.config(text=(f"Ваші гроші: {entryget}"))
            break
    else:
        messagebox.showinfo("Інформація!", "Помилка")
        

root = tk.Tk()
#налаштування
root.geometry("1920x1080")
root.minsize(50, 50)
root.resizable(False, False)
root.title("Застосунок")
#текста та все таке
label1 = tk.Label(root, text="Введіть скільки у вас грошей (треба 20000)")
entry = tk.Entry(root)
button1 = tk.Button(root, text="ок", command=numbers)
label_money = tk.Label(root, text=(f"Ваші гроші: невідомо"))
#cпавн
label1.pack()
entry.pack()
button1.pack()
label_money.pack()

root.mainloop()