# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


import math

num = int(input())

for i in range(2, int(math.sqrt(num)) + 1):
    while (num % i == 0):
        print(i)
        num //= i
if (num != 1):
    print(num)
