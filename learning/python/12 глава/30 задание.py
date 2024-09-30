# 12 глава - Задача 30
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали оргтехнику: Принтер")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали оргтехнику: Ксерокс")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали оргтехнику: Сканер")

# Создаем окно
root = tk.Tk()
root.title("Оргтехника")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите оргтехнику")
label.pack()

rb1 = tk.Radiobutton(root, text="Принтер", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Ксерокс", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Сканер", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
