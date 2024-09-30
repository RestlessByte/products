# 10 глава - Задача 15
def remove_extra_spaces(filename):
    with open(filename, "r") as f:
        text = f.read()
    cleaned_text = " ".join(text.split())
    with open("result_15.txt", "w") as f_out:
        f_out.write(cleaned_text)

if __name__ == "__main__":
    filename = "input.txt"
    remove_extra_spaces(filename)
