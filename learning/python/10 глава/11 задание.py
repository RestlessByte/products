# 10 глава - Задача 11
def replace_substring(filename, old, new):
    with open(filename, "r") as f:
        text = f.read()
    text = text.replace(old, new)
    with open("result_11.txt", "w") as f_out:
        f_out.write(text)

if __name__ == "__main__":
    filename = "input.txt"
    replace_substring(filename, "F", "Z")
