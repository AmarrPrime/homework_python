# Задача: предложить улучшения кода для уже решённых задач:
# - С помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# **Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

from functools import reduce

dot1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split())) 
dot2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))

def dot_range(dot1, dot2):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot1, dot2))))
     return round(rng, 2)
     
print(dot_range(dot1, dot2))