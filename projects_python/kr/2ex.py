from cgitb import text
import tkinter as tk
from turtle import color

root = tk.Tk()

#налаштування
root.geometry("1920x1080")
root.minsize(50, 50)
root.resizable(False, False)
root.title("Застосунок")

#кнопки
button1 = tk.Button(root, text="ок", bg="red")
button2 = tk.Button(root, text="ок???", bg="green", height="35", width="23")
button3 = tk.Button(root, text="ок!!!", bg="black", width="9")
button4 = tk.Button(root, text="ок&!&!$%&$&^$", bg="yellow", height="6")
button5 = tk.Button(root, text="УРААА ПЕРЕМОГА", bg="blue", )
button6 = tk.Button(root, text="окfdsg7dr7eg7ergyegrh4", bg="orange")
button7 = tk.Button(root, text="ок", bg="pink", height="12")

#спавн кнопок
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()

root.mainloop()