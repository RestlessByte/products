# 12 глава - Задача 22
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали: Уле Эйнар Бьорндален")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали: Майкл Фелпс")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали: Лариса Латынина")

# Создаем окно
root = tk.Tk()
root.title("Герои олимпиад")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите героя олимпиады")
label.pack()

rb1 = tk.Radiobutton(root, text="Уле Эйнар Бьорндален", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Майкл Фелпс", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Лариса Латынина", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
