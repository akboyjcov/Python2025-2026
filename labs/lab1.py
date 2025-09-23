import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')

x = np.arange(0.1, 20, 0.05)  
x = x[np.abs(np.sin(x)) > 0.01]  
x = x[np.abs(np.cos(x)) > 0.01]  

y_tan = np.tan(x)
y_ctg = 1 / np.tan(x)
y_product = 2 * y_tan * y_ctg  

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

ax1.plot(x, y_ctg, 'b-', linewidth=2)
ax1.set_title("Котангенс", fontsize=14)
ax1.set_xlabel("x", fontsize=12)
ax1.set_ylabel("ctg(x)", fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.set_ylim(-3.5, 3.5)

ax2.plot(x, y_tan, 'r-', linewidth=2, label='tg(x)')
ax2.plot(x, y_ctg, 'b--', linewidth=2, label='ctg(x)')
ax2.plot(x, y_product, 'g:', linewidth=3, label='2*tg(x)*ctg(x)')
ax2.set_title("Тригонометрические функции", fontsize=14)
ax2.set_xlabel("x", fontsize=12)
ax2.set_ylabel("y", fontsize=12)
ax2.legend(fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.set_ylim(-2.5, 3.5)

plt.tight_layout()
plt.show()

print(f"Диапазон x: от {x.min():.1f} до {x.max():.1f}")
print(f"Количество точек: {len(x)}")
print("2*tg(x)*ctg(x) всегда равно 2 (кроме особых точек)")