# 10 глава - Задача 13
def remove_text_in_parentheses(filename):
    with open(filename, "r") as f:
        text = f.read()
    while "(" in text and ")" in text:
        start = text.find("(")
        end = text.find(")")
        text = text[:start] + text[end+1:]
    with open("result_13.txt", "w") as f_out:
        f_out.write(text)

if __name__ == "__main__":
    filename = "input.txt"
    remove_text_in_parentheses(filename)
