from tkinter import *
import tkinter as tk

#функціі
def back():
    global current_track_index
    if current_track_index > 0:
        current_track_index -= 1
    else:
        current_track_index = len(musics) - 1
    label.config(text=f"Трек: {musics[current_track_index]}")

def stop():
    global stop_click
    if stop_click == 0:
        stop_click = 1
        label1.config(text="Трек на паузі")
    else:
        stop_click = 0
        label1.config(text="Трек не на паузі")

def next_song():
    global current_track_index
    if current_track_index < len(musics) - 1:
        current_track_index += 1
    else:
        current_track_index = 0
    label.config(text=f"Трек: {musics[current_track_index]}")

root = tk.Tk()
#налаштування
root.geometry("600x200")
root.minsize(50, 50)
root.resizable(False, False)
root.title("Застосунок")

#список
musics = ["Океан Ельзи - Відпусти", "Скрябін - Мам", "DZIDZIO - Шоу-бізнес", "Макс Барських - Туманы", "Тіна Кароль - Почему я жива",
          "Олег Винник - Колискова", "Монатик - Кружит", "MARUV - Siren Song", "Ірина Білик - Ти мій", "Друга Ріка - Відчуваю"]

#перемінні
current_track_index = 0
stop_click = 0

#текста та все таке
label = Label(root, text=f"Трек: {musics[current_track_index]}")
label1 = Label(root, text="Трек не на паузі")
btn1 = Button(root, text="Попередній трек", command=back)
btn2 = Button(root, text="Пауза", command=stop)
btn3 = Button(root, text="Наступний трек", command=next_song)
#cпавн
label.pack()
label1.pack()
btn1.pack()
btn2.pack()
btn3.pack()

root.mainloop()