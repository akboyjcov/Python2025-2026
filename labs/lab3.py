import matplotlib.pyplot as plt
import numpy as np

# Данные для построения диаграмм
months_temp = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн']
temperatures = [-5, -3, 12, 10, 18, 22]

income_sources = ['Зарплата', 'Фриланс', 'Инвестиции', 'Аренда']
income_percentages = [65, 15, 12, 8]

# Данные для заказов
orders_monthly = [2340, 2560, 2890, 3120]  # Заказы по месяцам
total_orders = sum(orders_monthly)  # Общая сумма = 10910

os_systems = ['Windows', 'macOS', 'Linux', 'Другие']
os_percentages = [68, 17, 9, 6]

# ПЕРВАЯ СТРАНИЦА: Средняя температура (ВЕРТИКАЛЬНАЯ) и распределение доходов
plt.figure(figsize=(14, 6))

# 1. ВЕРТИКАЛЬНАЯ столбчатая диаграмма средней температуры по месяцам
plt.subplot(1, 2, 1)
bars1 = plt.bar(months_temp, temperatures, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD'])
plt.title('Средняя температура по месяцам', fontsize=14, fontweight='bold')
plt.xlabel('Месяцы', fontsize=12)
plt.ylabel('Температура (°C)', fontsize=12)
plt.grid(axis='y', alpha=0.3)

# Добавляем значения на столбцы (вертикальная версия)
for bar, temp in zip(bars1, temperatures):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, f'{temp}°C', 
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# 2. Круговая диаграмма распределения источников дохода с ВЫДЕЛЕНИЕМ ВСЕХ СЕГМЕНТОВ
plt.subplot(1, 2, 2)
colors2 = ['#FF9999', '#66B3FF', '#99FF99', '#FFD700']
explode = (0.05, 0.05, 0.05, 0.05)  # Выделяем ВСЕ сегменты одинаково

plt.pie(income_percentages, labels=income_sources, autopct='%1.1f%%', 
        startangle=90, colors=colors2, explode=explode, shadow=True)
plt.title('Распределение источников дохода', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()

# ВТОРАЯ СТРАНИЦА: Количество заказов и доли операционных систем
plt.figure(figsize=(16, 6))

# 3. Столбчатая диаграмма количества заказов (как в примере)
plt.subplot(1, 2, 1)

# Позиции для столбцов (как в примере)
positions_monthly = [0.9, 1.9, 2.9, 3.9]      # Позиции для месячных заказов
positions_total = [1.1, 2.1, 3.1, 4.1]        # Позиции для общей суммы

# Все красные столбцы равны общей сумме 10910
orders_total = [total_orders, total_orders, total_orders, total_orders]

# Строим два набора столбцов со смещением
bars_total = plt.bar(positions_total, orders_total, width=0.2, color='#FF6B6B', label=f'Всего: {total_orders}')
bars_monthly = plt.bar(positions_monthly, orders_monthly, width=0.2, color='#4ECDC4', label='За месяц')

plt.title('Количество заказов в интернет-магазине', fontsize=14, fontweight='bold')
plt.xlabel('Месяцы', fontsize=12)
plt.ylabel('Количество заказов', fontsize=12)
plt.grid(axis='y', alpha=0.3)

# Подписи по оси X (только названия месяцев)
months_names = ["Январь", "Февраль", "Март", "Апрель"]
plt.xticks(positions_monthly, months_names)

# Добавляем значения на столбцы
for bar, value in zip(bars_monthly, orders_monthly):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 80, 
             f'{value}', ha='center', va='bottom', 
             fontsize=10, fontweight='bold')

for bar, value in zip(bars_total, orders_total):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 80, 
             f'{value}', ha='center', va='bottom', 
             fontsize=10, fontweight='bold')

# Добавляем легенду
plt.legend()

# 4. Круговая диаграмма в виде кольца (доли операционных систем)
plt.subplot(1, 2, 2)
colors4 = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#C9CBCF']

plt.pie(os_percentages, labels=os_systems, autopct='%1.1f%%', 
        startangle=90, colors=colors4, wedgeprops=dict(width=0.3))
plt.title('Доли операционных систем', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()