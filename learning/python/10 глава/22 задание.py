# 10 глава - Задача 22
def common_lines(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = set(f1.readlines())
        lines2 = set(f2.readlines())
    common = lines1 & lines2
    with open("result_22.txt", "w") as f_out:
        f_out.writelines(common)

if __name__ == "__main__":
    common_lines("file1.txt", "file2.txt")
