# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from math import pi

a = int(input("Введите количество символов точности числа пи: "))
print(f'Число пи с заданной точностью  равно {round(pi, a)}')