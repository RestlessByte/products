# 10 глава - Задача 9
def replace_letter(filename, old, new):
    with open(filename, "r") as f:
        text = f.read()
    text = text.replace(old, new)
    with open("result_9.txt", "w") as f_out:
        f_out.write(text)

if __name__ == "__main__":
    filename = "input.txt"
    replace_letter(filename, "a", "o")
