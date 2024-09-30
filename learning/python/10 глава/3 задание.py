# 10 глава - Задача 3
def find_longest_shortest(filename):
    with open(filename, "r") as f:
        words = f.read().split()
    longest = max(words, key=len)
    shortest = min(words, key=len)
    return longest, shortest

if __name__ == "__main__":
    filename = "input.txt"
    longest, shortest = find_longest_shortest(filename)
    print(f"Самое длинное слово: {longest}, самое короткое слово: {shortest}")
