# 12 глава - Задача 5
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали язык: Python")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали язык: Java")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали язык: C++")

# Создаем окно
root = tk.Tk()
root.title("Программирование")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите язык программирования")
label.pack()

rb1 = tk.Radiobutton(root, text="Python", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Java", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="C++", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
