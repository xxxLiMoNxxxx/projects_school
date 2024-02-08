from tkinter import *
import tkinter as tk

#функція
def plus():
    global clicks
    global plus_click
    clicks = clicks + plus_click
    label['text'] = str(clicks)
    if (clicks % 10 == 0):
        plus_click = plus_click + 1

root = tk.Tk()
#налаштування
root.geometry("1920x1080")
root.minsize(50, 50)
root.resizable(False, False)
root.title("Застосунок")
#переменная
clicks = 0
plus_click = 1

#текста та все таке
btn1 = Button(root, text="Клик", command=plus)
label = Label(root, text=str(clicks))
#cпавн
btn1.pack()
label.pack()

root.mainloop()