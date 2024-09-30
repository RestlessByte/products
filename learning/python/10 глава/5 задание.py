# 10 глава - Задача 5
def check_parentheses(filename):
    with open(filename, "r") as f:
        text = f.read()
    stack = []
    for char in text:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

if __name__ == "__main__":
    filename = "input.txt"
    result = check_parentheses(filename)
    with open("result_5.txt", "w") as f_out:
        f_out.write("Правильная расстановка скобок" if result else "Неправильная расстановка скобок")
