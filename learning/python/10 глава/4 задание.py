# 10 глава - Задача 4
def remove_duplicates(filename):
    with open(filename, "r") as f:
        text = f.read()
    unique_chars = "".join([c for c in text if text.count(c) == 1])
    with open("result_4.txt", "w") as f_out:
        f_out.write(unique_chars)

if __name__ == "__main__":
    filename = "input.txt"
    remove_duplicates(filename)
