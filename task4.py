N = int(input("Введите число N: "))
I = int(input("Введите начальное число I: "))

current = I
S = 0

while current <= N:
    S += current ** 2 
    current += 1      

print(f"Сумма квадратов чисел от {I} до {N}: S = {S}")