import math

print("Введите первую сторону треугольника")

x = float(input())
print("x =",x)

print("Введите вторую сторону треугольника")

y = float(input())
print("y =",y)

print("Введите угол между сторонами треугольника")

ang = float(input())
print("ang =",ang)

res = math.sqrt(x**2 + y**2 - 2*x*y*math.cos(math.radians(ang)))

print("Длина третьей стороны равна", res)