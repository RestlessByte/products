# 10 глава - Задача 24
def remove_words(filename, words_to_remove):
    with open(filename, "r") as f:
        text = f.read()
    for word in words_to_remove:
        text = text.replace(word, "")
    with open("result_24.txt", "w") as f_out:
        f_out.write(text)

if __name__ == "__main__":
    filename = "input.txt"
    words_to_remove = ["слово1", "слово2"]
    remove_words(filename, words_to_remove)
