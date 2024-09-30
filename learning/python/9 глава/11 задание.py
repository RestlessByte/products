# 9 глава - Задача 11
def compare_products(A, B):
    product_A = 1
    for num in A:
        product_A *= num
    
    product_B = 1
    for num in B:
        product_B *= num
    
    if product_A > product_B:
        return "Список A имеет большее произведение."
    elif product_B > product_A:
        return "Список B имеет большее произведение."
    else:
        return "Произведения списков A и B равны."

if __name__ == "__main__":
    A = [1, 2, 3]
    B = [2, 3, 4]
    result = compare_products(A, B)
    print(result)
