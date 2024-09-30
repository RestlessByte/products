# 6 глава - Задача 24
# Программа для определения, имеются ли игроки одинакового роста в двух командах
team1_heights = tuple(map(int, input("Введите росты игроков первой команды через пробел: ").split()))
team2_heights = tuple(map(int, input("Введите росты игроков второй команды через пробел: ").split()))

common_heights = set(team1_heights) & set(team2_heights)

if common_heights:
    print(f"Игроки одинакового роста: {common_heights}")
else:
    print("Игроков одинакового роста нет")
