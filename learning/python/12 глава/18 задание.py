# 12 глава - Задача 18
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали животное: Кошка")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали животное: Собака")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали животное: Попугай")

# Создаем окно
root = tk.Tk()
root.title("Домашние животные")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите домашнее животное")
label.pack()

rb1 = tk.Radiobutton(root, text="Кошка", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Собака", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Попугай", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
