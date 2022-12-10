from random import randint
from random import choice


def show_field():
    global field
    for i in range(0, len(field), 3):
        print(field[i], field[i+1], field[i+2])


def input_pos():
    global field
    while True:
        position = int(input('Введите позицию: '))
        if type(field[position-1]) == int and 1 <= position <= 9:
            field[position-1] = 'X'
            break
        else:
            print('Позиция занята')


def bot_move():
    global field
    while True:
        position = randint(0, 8)
        if type(field[position]) == int:
            field[position] = 'O'
            break


def is_victory(field):
    vin = False
    combs = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]
    for pos in combs:
        if field[pos[0]] == field[pos[1]] == field[pos[2]]:
            vin = True
            break
    return vin


def spare(field):
    count = 0
    for i in field:
        if type(i) == str:
            count += 1
    if count == 9:
        return True
    else:
        return False


field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

players = ['Пользователь', "Компьютер"]
move = choice(players)
print(f'Первым ходит - {move}')
print('-'*10)
show_field()
print('-'*10)


while True:
    if move == 'Пользователь':
        print('-'*10)
        input_pos()
        show_field()
        print('-'*10)
        move = "Компьютер"
        if is_victory(field):
            print('Пользователь победил')
            break
    else:
        bot_move()
        print('Бот сделал ход')
        show_field()
        print('-'*10)
        move = 'Пользователь'
        if is_victory(field):
            print('Робот победил')
            break
    if spare(field):
        print('Ничья')
        break
