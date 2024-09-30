# 10 глава - Задача 17
def count_negative_in_rows(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    with open("result_17.txt", "w") as f_out:
        for line in lines:
            numbers = list(map(int, line.split()))
            negative_count = sum(1 for num in numbers if num < 0)
            f_out.write(f"Количество отрицательных чисел: {negative_count}\n")

if __name__ == "__main__":
    filename = "input_numbers.txt"
    count_negative_in_rows(filename)
