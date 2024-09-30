# 12 глава - Задача 10
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали мотоцикл: Harley-Davidson")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали мотоцикл: Yamaha")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали мотоцикл: Kawasaki")

# Создаем окно
root = tk.Tk()
root.title("Мотоциклы")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите мотоцикл")
label.pack()

rb1 = tk.Radiobutton(root, text="Harley-Davidson", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Yamaha", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Kawasaki", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
