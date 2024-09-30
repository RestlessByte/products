# 12 глава - Задача 8
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали достопримечательность: Красная площадь")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали достопримечательность: Эрмитаж")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали достопримечательность: Кремль")

# Создаем окно
root = tk.Tk()
root.title("Достопримечательности моего города")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите достопримечательность")
label.pack()

rb1 = tk.Radiobutton(root, text="Красная площадь", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Эрмитаж", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Кремль", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
