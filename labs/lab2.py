import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 1000)
x_clean = np.linspace(-3, 3, 1000)
x_clean = x_clean[np.abs(x_clean) > 0.01] 

y1 = x**2 * np.exp(x**2)
y2 = np.log(x_clean**2)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y1, 'b-', linewidth=2, label=r'$y = x^2 \cdot e^{x^2}$')
plt.plot(x_clean, y2, 'r-', linewidth=2, label=r'$y = \ln(x^2)$')
plt.title('Графики функций', fontsize=14, fontweight='bold')
plt.xlabel('x (радианы)', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim(-3, 3)

radian_labels = [r'$-\pi$', r'$-\frac{2\pi}{3}$', r'$-\frac{\pi}{3}$', '0', 
                 r'$\frac{\pi}{3}$', r'$\frac{2\pi}{3}$', r'$\pi$']
radian_positions = [-np.pi, -2*np.pi/3, -np.pi/3, 0, np.pi/3, 2*np.pi/3, np.pi]
plt.xticks(radian_positions, radian_labels)

plt.subplot(2, 2, 2)
x_points1 = np.linspace(-2, 2, 15)
y_points1 = x_points1**2 * np.exp(x_points1**2)
plt.plot(x, y1, 'b-', alpha=0.5)
plt.plot(x_points1, y_points1, 'bo', markersize=6, label='Точки от -2 до 2')
plt.title(r'$y = x^2 \cdot e^{x^2}$ - центральные точки', fontsize=12)
plt.xlabel('x (радианы)')
plt.ylabel('y')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(radian_positions, radian_labels)

plt.subplot(2, 2, 3)
x_points2 = np.linspace(-1.5, 1.5, 12)
y_points2 = x_points2**2 * np.exp(x_points2**2)
plt.plot(x, y1, 'b-', alpha=0.5)
plt.plot(x_points2, y_points2, 'ro', markersize=6, label='Точки от -1.5 до 1.5')
plt.title(r'$y = x^2 \cdot e^{x^2}$ - узкий центр', fontsize=12)
plt.xlabel('x (радианы)')
plt.ylabel('y')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(radian_positions, radian_labels)

plt.subplot(2, 2, 4)
x_points3 = np.linspace(-1, 1, 10)
y_points3 = x_points3**2 * np.exp(x_points3**2)
plt.plot(x, y1, 'b-', alpha=0.5)
plt.plot(x_points3, y_points3, 'go', markersize=6, label='Точки от -1 до 1')
plt.title(r'$y = x^2 \cdot e^{x^2}$ - вокруг нуля', fontsize=12)
plt.xlabel('x (радианы)')
plt.ylabel('y')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(radian_positions, radian_labels)

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))

radian_labels_simple = [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$']
radian_positions_simple = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]

plt.subplot(2, 3, 1)
x2_points1 = np.linspace(-2, 2, 20)
x2_points1 = x2_points1[np.abs(x2_points1) > 0.1] 
y2_points1 = np.log(x2_points1**2)
plt.plot(x_clean, y2, 'r-', alpha=0.5)
plt.plot(x2_points1, y2_points1, 'bo', markersize=5, label='Точки от -2 до 2')
plt.title(r'$y = \ln(x^2)$ - центральные точки', fontsize=12)
plt.xlabel('x (радианы)')
plt.ylabel('y')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(radian_positions_simple, radian_labels_simple)

plt.subplot(2, 3, 2)
x2_points2 = np.linspace(-1.5, 1.5, 15)
x2_points2 = x2_points2[np.abs(x2_points2) > 0.1]
y2_points2 = np.log(x2_points2**2)
plt.plot(x_clean, y2, 'r-', alpha=0.5)
plt.plot(x2_points2, y2_points2, 'ro', markersize=5, label='Точки от -1.5 до 1.5')
plt.title(r'$y = \ln(x^2)$ - узкий центр', fontsize=12)
plt.xlabel('x (радианы)')
plt.ylabel('y')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(radian_positions_simple, radian_labels_simple)

plt.subplot(2, 3, 3)
x2_points3 = np.linspace(-1, 1, 12)
x2_points3 = x2_points3[np.abs(x2_points3) > 0.1]
y2_points3 = np.log(x2_points3**2)
plt.plot(x_clean, y2, 'r-', alpha=0.5)
plt.plot(x2_points3, y2_points3, 'go', markersize=5, label='Точки от -1 до 1')
plt.title(r'$y = \ln(x^2)$ - вокруг нуля', fontsize=12)
plt.xlabel('x (радианы)')
plt.ylabel('y')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(radian_positions_simple, radian_labels_simple)

plt.subplot(2, 3, 4)
x2_points4 = np.concatenate([
    np.linspace(-2, -0.5, 8),  
    np.linspace(0.5, 2, 8)     
])
y2_points4 = np.log(x2_points4**2)
plt.plot(x_clean, y2, 'r-', alpha=0.5)
plt.plot(x2_points4, y2_points4, 'mo', markersize=5, label='Две центральные области')
plt.title(r'$y = \ln(x^2)$ - две области', fontsize=12)
plt.xlabel('x (радианы)')
plt.ylabel('y')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(radian_positions_simple, radian_labels_simple)

plt.subplot(2, 3, 5)
x2_points5 = np.linspace(-1.8, 1.6, 14)
x2_points5 = x2_points5[np.abs(x2_points5) > 0.1]
y2_points5 = np.log(x2_points5**2)
plt.plot(x_clean, y2, 'r-', alpha=0.5)
plt.plot(x2_points5, y2_points5, 'co', markersize=5, label='Несимметричный центр')
plt.title(r'$y = \ln(x^2)$ - несимметрично', fontsize=12)
plt.xlabel('x (радианы)')
plt.ylabel('y')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(radian_positions_simple, radian_labels_simple)

plt.subplot(2, 3, 6)
x2_points6 = np.linspace(-0.8, 0.8, 10)
x2_points6 = x2_points6[np.abs(x2_points6) > 0.1]
y2_points6 = np.log(x2_points6**2)
plt.plot(x_clean, y2, 'r-', alpha=0.5)
plt.plot(x2_points6, y2_points6, 'yo', markersize=5, label='Очень узкий центр')
plt.title(r'$y = \ln(x^2)$ - очень узко', fontsize=12)
plt.xlabel('x (радианы)')
plt.ylabel('y')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(radian_positions_simple, radian_labels_simple)

plt.tight_layout()
plt.show()