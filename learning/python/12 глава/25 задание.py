# 12 глава - Задача 25
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали животное: Лев")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали животное: Тигр")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали животное: Медведь")

# Создаем окно
root = tk.Tk()
root.title("Дикие животные")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите дикое животное")
label.pack()

rb1 = tk.Radiobutton(root, text="Лев", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Тигр", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Медведь", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
