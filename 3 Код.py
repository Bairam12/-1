import math

a = float(input())
b = float(input())

# Гипотенуза
c = math.sqrt(a**2 + b**2)

# Площадь
S = (a * b) / 2

# Периметр
P = a + b + c

# Углы
angle_a = math.degrees(math.atan(a / b))
angle_b = math.degrees(math.atan(b / a))

print("Гипотенуза:", c)
print("Площадь:", S)
print("Периметр:", P)
print("Первый острый угол:", angle_a)
print("Второй острый угол:", angle_b)
