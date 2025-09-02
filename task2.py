def get_age_end(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

N = int(input("Введите возраст человека (1-100): "))

if N < 1 or N > 100:
    print("Ошибка! Возраст должен быть от 1 до 100 лет")
else:
    end = get_age_end(N)
    print(f"{N} {end}")