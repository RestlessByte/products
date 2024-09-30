# 12 глава - Задача 28
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали сказку: Колобок")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали сказку: Теремок")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали сказку: Репка")

# Создаем окно
root = tk.Tk()
root.title("Русские народные сказки")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите народную сказку")
label.pack()

rb1 = tk.Radiobutton(root, text="Колобок", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Теремок", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Репка", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
