# 12 глава - Задача 7
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали город: Москва")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали город: Санкт-Петербург")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали город: Казань")

# Создаем окно
root = tk.Tk()
root.title("Города России")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите город")
label.pack()

rb1 = tk.Radiobutton(root, text="Москва", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Санкт-Петербург", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Казань", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
