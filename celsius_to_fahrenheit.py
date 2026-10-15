celsium = "CcСс"
farenheit = "Ff"
x = input()

if x[-1:] in celsium:
    y = 9/5*float(x[:-1]) + 32
    print(f"Температура в фаренгейтах: {y}")
elif x[-1:] in farenheit:
    y = 5/9*(float(x[:-1]) - 32)
    print(f"Температура в градусах цельсия: {y}")
