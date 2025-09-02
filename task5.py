import math

n = int(input("Введите n: "))

for i in range(1, n + 1):
    result = math.cos(i**3) * math.sin(i * n)
    if abs(result) < 0.0001:
        print(f"i = {i}: {result}")