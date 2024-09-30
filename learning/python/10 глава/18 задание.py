# 10 глава - Задача 18
def find_min_in_rows(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    with open("result_18.txt", "w") as f_out:
        for line in lines:
            numbers = list(map(int, line.split()))
            min_index = numbers.index(min(numbers))
            f_out.write(f"Индекс минимального числа: {min_index}\n")

if __name__ == "__main__":
    filename = "input_numbers.txt"
    find_min_in_rows(filename)
