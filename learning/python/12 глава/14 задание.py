# 12 глава - Задача 14
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали фильм: Властелин колец")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали фильм: Гарри Поттер")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали фильм: Матрица")

# Создаем окно
root = tk.Tk()
root.title("Зарубежное кино")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите фильм")
label.pack()

rb1 = tk.Radiobutton(root, text="Властелин колец", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Гарри Поттер", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Матрица", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
