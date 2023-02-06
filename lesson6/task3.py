#  С помощью использования лямбд, filter, map, zip, enumerate, list comprehension
#  Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

import random

a = [random.randint(1,10) for i in range(5)]
res = [a[indx]*a[-indx-1] for indx in range(len(a)//2+len(a)%2)]
print(a)
print(res)