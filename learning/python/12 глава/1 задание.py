# 12 глава - Задача 1
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали фильм: Брат")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали фильм: Москва слезам не верит")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали фильм: Служебный роман")

# Создаем окно
root = tk.Tk()
root.title("Российские кинофильмы")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите российский фильм")
label.pack()

rb1 = tk.Radiobutton(root, text="Брат", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Москва слезам не верит", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Служебный роман", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
