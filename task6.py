import math

A = 20
B = 10
angle = 45 

h = ((A - B) / 2) / math.tan(math.radians(angle))
S = (A + B) / 2 * h

print(f"Площадь трапеции: {S:.4f}")