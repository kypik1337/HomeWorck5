import random
# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

player1 = ""

counter1 = 0 
counter2 = 0
value = 150

ocher = random.randint(0,2) # ставим рандомную очередность 
if ocher:
    print(f"Первый ходит player")
else:
    print(f"Первый ходит compyter")

    while value > 28:     # погнал цикл решения 
        if ocher:
            k = input_dat(player1)
            counter1 += k
            ocher = False
            print (f"Ходил player, он взял {k}, теперь у него {counter1}. Осталось на столе {value} конфет.")
        else:
            k = random.randint(0, 28)
            counter2 += k
            value -= k
            ocher = True
            print(f"Ходил compyter, он взял {k}, теперь у него {counter2}. Осталось на столе {value} конфет.")

if ocher:
    print(f"Выиграл player1")
else:
    print(f"Выиграл computer")