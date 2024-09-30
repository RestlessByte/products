# 9 глава - Задача 23
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def max_digit_sum(A):
    return max(A, key=sum_of_digits)

if __name__ == "__main__":
    A = [123, 456, 789]
    result = max_digit_sum(A)
    print(f"Число с максимальной суммой цифр: {result}")
