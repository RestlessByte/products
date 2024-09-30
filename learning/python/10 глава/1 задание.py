# 10 глава - Задача 1
def count_double_letters(filename):
    with open(filename, "r") as f:
        text = f.read()
    doubles = ["аа", "оо", "кк"]
    count = sum(text.count(pair) for pair in doubles)
    unique_text = text.replace("аа", "а").replace("оо", "о").replace("кк", "к")
    with open("result_1.txt", "w") as f_out:
        f_out.write(unique_text)
    return count

if __name__ == "__main__":
    filename = "input.txt"
    count = count_double_letters(filename)
    print(f"Количество сдвоенных символов: {count}")
