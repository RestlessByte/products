# 12 глава - Задача 13
import tkinter as tk
from tkinter import messagebox

def show_result():
    selected = var.get()
    if selected == 1:
        messagebox.showinfo("Результат", "Вы выбрали мультфильм: Ну, погоди!")
    elif selected == 2:
        messagebox.showinfo("Результат", "Вы выбрали мультфильм: Винни-Пух")
    elif selected == 3:
        messagebox.showinfo("Результат", "Вы выбрали мультфильм: Маша и Медведь")

# Создаем окно
root = tk.Tk()
root.title("Мультфильмы")

# Варианты для выбора
var = tk.IntVar()

label = tk.Label(root, text="Выберите мультфильм")
label.pack()

rb1 = tk.Radiobutton(root, text="Ну, погоди!", variable=var, value=1)
rb1.pack()
rb2 = tk.Radiobutton(root, text="Винни-Пух", variable=var, value=2)
rb2.pack()
rb3 = tk.Radiobutton(root, text="Маша и Медведь", variable=var, value=3)
rb3.pack()

button = tk.Button(root, text="Подтвердить выбор", command=show_result)
button.pack()

root.mainloop()
