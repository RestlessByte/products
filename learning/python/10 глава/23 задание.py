# 10 глава - Задача 23
def append_file_info(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    line_count = len(lines)
    with open(filename, "a") as f_out:
        f_out.write(f"\nКоличество строк: {line_count}\n")
        for i, line in enumerate(lines):
            char_count = len(line.strip())
            digit_count = sum(c.isdigit() for c in line)
            f_out.write(f"Строка {i+1}: {char_count} символов, {digit_count} цифр\n")

if __name__ == "__main__":
    filename = "input.txt"
    append_file_info(filename)
