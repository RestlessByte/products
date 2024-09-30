# 12 глава - Задача 3
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали: Lada")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали: BMW")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали: Mercedes")

# Создаем окно
root = tk.Tk()
root.title("Автомобили")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите марку автомобиля")
label.pack()

rb1 = tk.Radiobutton(root, text="Lada", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="BMW", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Mercedes", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
