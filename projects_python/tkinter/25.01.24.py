import tkinter as tk

def click():
    label4.config(text="dsfgrftgyuthgucx fdtgrskl.;mcgbbvcm")

def button(event):
    global font_size
    font_size += 5
    label4.config(font=f"Arial {font_size}")
def button_minus(event):
    global font_size
    font_size -= 5
    label4.config(font=f"Arial {font_size}")
def del_all(event):
    for widget in root.winfo_children(): 
        widget.destroy() 

font_size = 10
root = tk.Tk()

root.geometry("720x1280")
root.title("fdgdfgdfg")

label4 = tk.Label(root, text="dfhgfdjhjghghkghk")
button4 = tk.Button(root, text="gfdfdhdfh", command=click)
label2 = tk.Label(root, text="dfhgfdjhjghghkghk", background="#000")

button4.bind("<Button-1>", button)
button4.bind("<Button-3>", button_minus)
root.bind("<F2>", del_all)
label4.pack()
button4.pack()

root.mainloop()