# 9 глава - Задача 17
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def count_primes(A):
    return sum(1 for num in A if is_prime(num))

if __name__ == "__main__":
    A = [2, 3, 4, 5, 6, 7]
    prime_count = count_primes(A)
    print(f"Количество простых чисел в списке A: {prime_count}")
