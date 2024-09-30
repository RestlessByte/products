# 12 глава - Задача 15
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали артиста: Майкл Джексон")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали артиста: Мадонна")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали артиста: Элтон Джон")

# Создаем окно
root = tk.Tk()
root.title("Зарубежная эстрада")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите артиста")
label.pack()

rb1 = tk.Radiobutton(root, text="Майкл Джексон", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Мадонна", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Элтон Джон", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
