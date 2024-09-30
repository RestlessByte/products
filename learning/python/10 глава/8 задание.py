# 10 глава - Задача 8
def common_chars(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    if len(lines) < 2:
        return
    common = set(lines[0].strip()) & set(lines[1].strip())
    with open("result_8.txt", "w") as f_out:
        f_out.write("".join(common))

if __name__ == "__main__":
    filename = "input.txt"
    common_chars(filename)
