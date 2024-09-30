# 12 глава - Задача 29
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали балерину: Майя Плисецкая")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали балерину: Анна Павлова")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали балерину: Галина Уланова")

# Создаем окно
root = tk.Tk()
root.title("Легенды российского балета")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите легенду российского балета")
label.pack()

rb1 = tk.Radiobutton(root, text="Майя Плисецкая", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Анна Павлова", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Галина Уланова", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
