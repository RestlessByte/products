# 10 глава - Задача 20
def avg_positive_numbers(filename):
    with open(filename, "r") as f:
        numbers = list(map(int, f.read().split()))
    positive_numbers = [num for num in numbers if num > 0]
    average = sum(positive_numbers) / len(positive_numbers) if positive_numbers else 0
    with open("result_20.txt", "w") as f_out:
        f_out.write(f"Среднее арифметическое положительных чисел: {average:.2f}\n")

if __name__ == "__main__":
    filename = "input_numbers.txt"
    avg_positive_numbers(filename)
