# Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. 
# Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил
#  Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 



from random import randint


def number_input(name):
    x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, total):
    print(f"{name} взял {k}, теперь у него {counter}. Осталось на столе {total} конфет.")


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
total = int(input("Введите количество конфет на столе: "))
order = randint(0, 2)
if order:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while total > 28:
    if order:
        k = number_input(player1)
        counter1 += k
        total -= k
        order = False
        p_print(player1, k, counter1, total)
    else:
        k = number_input(player2)
        counter2 += k
        total -= k
        order = True
        p_print(player2, k, counter2, total)

if order:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")