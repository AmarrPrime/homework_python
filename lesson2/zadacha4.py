# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных 
# позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.

import random

n= int(input())
list_num = [random.randint(-n,n) for i in range (n)]
print(list_num)

file = open("file.txt","r")
mult = 1

for i in file:
    mult*=list_num[int(i)]
print(mult)