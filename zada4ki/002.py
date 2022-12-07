#Создайте программу для игры в ""Крестики-нолики"".


setka = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def printSetka (set):
    print(f'{setka[0]} | {setka[1]} | {setka[2]}')
    print('---------')
    print(f'{setka[3]} | {setka[4]} | {setka[5]}')
    print('---------')
    print(f'{setka[6]} | {setka[7]} | {setka[8]}')

print(printSetka(setka))

def take_input (player_token):    #оргумент функции
    valid = False
    while not valid:   #меняет результат тоесть если будет тру то он поменяет на фолс и обратно
        player_answer = input(' куда поставим ' + player_token + "?")

        try:
            player_answer = int(player_answer)
        except:
            print('не корректный ввод')
            continue
        if player_answer >= 1 and player_answer <= 9 :
            if(str(setka[player_answer -1]) not in 'XO'):
                setka[player_answer -1] = player_token
                valid = True
            else:
                print('клетка уже занята ')
        else:
            print('введите число от 1 до 9')









# while True:
#     per1 = int(input('Введи позицию для крестика X:= ') )
#     setka[per1-1] = 'X'
#     print(printSetka(setka))
#     per2 = int(input('Введи позицию для крестика 0:= ') )
#     setka[per2-1] = '0'
#     print(printSetka(setka))
#     if per1 == setka[per1-1] and per2 == setka[per2-1] :
#         print('Эта позиция уже занята!')
    
