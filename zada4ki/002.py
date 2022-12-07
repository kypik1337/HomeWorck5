#Создайте программу для игры в ""Крестики-нолики"".


setka = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def printSetka (set):
    print(f'{setka[0]} | {setka[1]} | {setka[2]}')
    print('---------')
    print(f'{setka[3]} | {setka[4]} | {setka[5]}')
    print('---------')
    print(f'{setka[6]} | {setka[7]} | {setka[8]}')

print(printSetka(setka))

while True:
    per1 = int(input('Введи позицию для крестика X:= ') )
    setka[per1-1] = 'X'
    print(printSetka(setka))
    per2 = int(input('Введи позицию для крестика 0:= ') )
    setka[per2-1] = '0'
    print(printSetka(setka))
    