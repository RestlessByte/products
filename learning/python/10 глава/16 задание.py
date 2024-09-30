# 10 глава - Задача 16
def sum_even_numbers_in_rows(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    with open("result_16.txt", "w") as f_out:
        for line in lines:
            numbers = list(map(int, line.split()))
            even_sum = sum(num for num in numbers if num % 2 == 0)
            f_out.write(f"Сумма четных чисел: {even_sum}\n")

if __name__ == "__main__":
    filename = "input_numbers.txt"
    sum_even_numbers_in_rows(filename)
