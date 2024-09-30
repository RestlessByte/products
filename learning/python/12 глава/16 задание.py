# 12 глава - Задача 16
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали технику: Танк Т-34")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали технику: Истребитель Су-27")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали технику: Ракетный комплекс С-400")

# Создаем окно
root = tk.Tk()
root.title("Военная техника")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите военную технику")
label.pack()

rb1 = tk.Radiobutton(root, text="Танк Т-34", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Истребитель Су-27", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Ракетный комплекс С-400", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
