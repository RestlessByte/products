# 12 глава - Задача 26
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали актера: Сергей Безруков")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали актера: Данила Козловский")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали актера: Константин Хабенский")

# Создаем окно
root = tk.Tk()
root.title("Российские киноактеры")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите российского киноактера")
label.pack()

rb1 = tk.Radiobutton(root, text="Сергей Безруков", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Данила Козловский", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Константин Хабенский", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
