# 10 глава - Задача 2
def count_words(filename):
    with open(filename, "r") as f:
        text = f.read()
    words = text.split()
    return len(words)

if __name__ == "__main__":
    filename = "input.txt"
    word_count = count_words(filename)
    print(f"Количество слов: {word_count}")
