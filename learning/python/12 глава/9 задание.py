# 12 глава - Задача 9
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали: Борщ")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали: Оливье")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали: Пельмени")

# Создаем окно
root = tk.Tk()
root.title("Кулинария")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите блюдо")
label.pack()

rb1 = tk.Radiobutton(root, text="Борщ", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Оливье", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Пельмени", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
