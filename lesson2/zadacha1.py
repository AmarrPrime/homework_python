# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


a = float(input())
sum = 0
while a != int(a):
    a = round(a*10, len(str(a))-1)
print(a)

while a > 0:
    sum += a % 10
    a = a//10
print(sum)