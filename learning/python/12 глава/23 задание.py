# 12 глава - Задача 23
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали период: Древняя Русь")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали период: Царская Россия")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали период: СССР")

# Создаем окно
root = tk.Tk()
root.title("История России")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите период истории России")
label.pack()

rb1 = tk.Radiobutton(root, text="Древняя Русь", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Царская Россия", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="СССР", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
