# 10 глава - Задача 10
def reverse_words(filename):
    with open(filename, "r") as f:
        words = f.read().split()
    reversed_words = [word[::-1] for word in words]
    with open("result_10.txt", "w") as f_out:
        f_out.write(" ".join(reversed_words))

if __name__ == "__main__":
    filename = "input.txt"
    reverse_words(filename)
