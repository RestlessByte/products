# 12 глава - Задача 2
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали: Футбол")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали: Хоккей")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали: Теннис")

# Создаем окно
root = tk.Tk()
root.title("Спорт")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите вид спорта")
label.pack()

rb1 = tk.Radiobutton(root, text="Футбол", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Хоккей", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Теннис", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
