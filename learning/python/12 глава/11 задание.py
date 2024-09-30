# 12 глава - Задача 11
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали художника: Леонардо да Винчи")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали художника: Ван Гог")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали художника: Пабло Пикассо")

# Создаем окно
root = tk.Tk()
root.title("Живопись")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите художника")
label.pack()

rb1 = tk.Radiobutton(root, text="Леонардо да Винчи", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Ван Гог", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Пабло Пикассо", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
