# 10 глава - Задача 7
def swap_first_last_words(filename):
    with open(filename, "r") as f:
        words = f.read().split()
    if len(words) < 2:
        return
    words[0], words[-1] = words[-1], words[0]
    with open("result_7.txt", "w") as f_out:
        f_out.write(" ".join(words))

if __name__ == "__main__":
    filename = "input.txt"
    swap_first_last_words(filename)
