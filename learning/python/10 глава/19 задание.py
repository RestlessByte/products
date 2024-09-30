# 10 глава - Задача 19
def find_first_even_in_rows(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    with open("result_19.txt", "w") as f_out:
        for line in lines:
            numbers = list(map(int, line.split()))
            even_index = next((i for i, num in enumerate(numbers) if num % 2 == 0), -1)
            f_out.write(f"Индекс первого четного числа: {even_index}\n")

if __name__ == "__main__":
    filename = "input_numbers.txt"
    find_first_even_in_rows(filename)
