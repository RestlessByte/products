# 10 глава - Задача 6
def count_symbols(filename):
    with open(filename, "r") as f:
        text = f.read()
    count = sum(text.count(symbol) for symbol in ["+", "-", "*"])
    return count

if __name__ == "__main__":
    filename = "input.txt"
    count = count_symbols(filename)
    print(f"Количество символов +, -, *: {count}")
