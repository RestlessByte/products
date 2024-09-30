# 10 глава - Задача 12
def count_symbol_occurrences(filename, symbol):
    with open(filename, "r") as f:
        text = f.read()
    count = text.count(symbol)
    with open("result_12.txt", "w") as f_out:
        f_out.write(f"Количество символов {symbol}: {count}")

if __name__ == "__main__":
    filename = "input.txt"
    count_symbol_occurrences(filename, "a")
