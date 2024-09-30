# 10 глава - Задача 14
def remove_single_letter_words(filename):
    with open(filename, "r") as f:
        words = f.read().split()
    words = [word for word in words if len(word) > 1]
    with open("result_14.txt", "w") as f_out:
        f_out.write(" ".join(words))

if __name__ == "__main__":
    filename = "input.txt"
    remove_single_letter_words(filename)
