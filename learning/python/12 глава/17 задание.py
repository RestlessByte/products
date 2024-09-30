# 12 глава - Задача 17
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали композитора: Бах")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали композитора: Моцарт")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали композитора: Бетховен")

# Создаем окно
root = tk.Tk()
root.title("Классическая музыка")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите композитора")
label.pack()

rb1 = tk.Radiobutton(root, text="Бах", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Моцарт", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Бетховен", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
