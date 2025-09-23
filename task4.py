n = int(input("Введите количество чисел: "))

if n <= 0:
    print("Ошибка: количество чисел должно быть положительным")
else:
    total = 0.0
    
    print("Введите числа:")
    for i in range(n):
        num = float(input(f"Число {i+1}: "))
        total += num
    
    average = total / n
    
    print(f"\nСумма чисел: {total}")
    print(f"Количество чисел: {n}")
    print(f"Среднее арифметическое: {average:.2f}")