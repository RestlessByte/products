# 12 глава - Задача 27
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали сайт: Wikipedia")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали сайт: Google")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали сайт: YouTube")

# Создаем окно
root = tk.Tk()
root.title("Интернет")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите популярный интернет-ресурс")
label.pack()

rb1 = tk.Radiobutton(root, text="Wikipedia", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Google", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="YouTube", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
