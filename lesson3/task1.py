# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

list_num = [randint(0, 10) for i in range(randint(5, 10))]
print(list_num)
sum = 0
for i in range(1, len(list_num), 2):
    sum += list_num[i]
print(sum)
