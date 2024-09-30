# 12 глава - Задача 24
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали поэта: Александр Пушкин")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали поэта: Сергей Есенин")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали поэта: Анна Ахматова")

# Создаем окно
root = tk.Tk()
root.title("Русские поэты")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите поэта")
label.pack()

rb1 = tk.Radiobutton(root, text="Александр Пушкин", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Сергей Есенин", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Анна Ахматова", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
