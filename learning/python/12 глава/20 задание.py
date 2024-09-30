# 12 глава - Задача 20
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали: Тихий океан")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали: Атлантический океан")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали: Индийский океан")

# Создаем окно
root = tk.Tk()
root.title("Моря и океаны")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите океан")
label.pack()

rb1 = tk.Radiobutton(root, text="Тихий океан", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Атлантический океан", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Индийский океан", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
