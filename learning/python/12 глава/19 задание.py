# 12 глава - Задача 19
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали тему: Алгоритмы")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали тему: Базы данных")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали тему: Программирование")

# Создаем окно
root = tk.Tk()
root.title("Информатика")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите тему информатики")
label.pack()

rb1 = tk.Radiobutton(root, text="Алгоритмы", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Базы данных", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Программирование", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
