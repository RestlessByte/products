# 12 глава - Задача 12
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали книгу: Война и мир")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали книгу: Преступление и наказание")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали книгу: Анна Каренина")

# Создаем окно
root = tk.Tk()
root.title("Книги")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите книгу")
label.pack()

rb1 = tk.Radiobutton(root, text="Война и мир", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Преступление и наказание", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Анна Каренина", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
