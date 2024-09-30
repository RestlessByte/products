# 10 глава - Задача 21
def max_min_difference(filename):
    with open(filename, "r") as f:
        numbers = list(map(int, f.read().split()))
    difference = max(numbers) - min(numbers)
    with open("result_21.txt", "w") as f_out:
        f_out.write(f"Разность между максимальным и минимальным: {difference}\n")

if __name__ == "__main__":
    filename = "input_numbers.txt"
    max_min_difference(filename)
