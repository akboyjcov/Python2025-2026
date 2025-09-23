import random

def matrix_column_averages(n):
    matrix = []
    
    print(f"Матрица {n} x 9:")
    print("-" * 50)
    
    for i in range(n):
        row = [round(random.uniform(0, 100), 1) for _ in range(9)]
        matrix.append(row)
        print(f"Строка {i+1}: {row}")
    
    column_averages = []
    
    print("\nВычисление средних арифметических:")
    print("-" * 50)
    
    for col in range(9):
        column_sum = 0
        for row in range(n):
            column_sum += matrix[row][col]
        
        average = column_sum / n
        column_averages.append(average)
        
        print(f"Столбец {col+1}: сумма = {column_sum:.2f}, среднее = {average:.2f}")
    
    return matrix, column_averages

try:
    n = int(input("Введите натуральное число n (количество строк): "))
    
    if n <= 0:
        print("Ошибка: n должно быть натуральным числом")
    else:
        matrix, averages = matrix_column_averages(n)
        
        print("\nРезультат:")
        print("-" * 30)
        for i, avg in enumerate(averages, 1):
            print(f"Столбец {i}: среднее = {avg:.2f}")

except ValueError:
    print("Ошибка: введите целое число")