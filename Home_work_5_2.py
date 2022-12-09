# 2. Создайте программу для игры в ""Крестики-нолики"".
# (в консоли происходит выбор позиции)

board = list(range(1, 10))


def PrintBoard(board: list):
    """Рисует игровое поле"""
    for i in range(3):
        print(board[0+i*3], board[1+i*3], board[2+i*3])


def PlayerInput(PlayerEnt: int):
    """Принимает ввод пользователя. Проверяет корректность ввода."""
    valid = False
    while not valid:
        PlayerAnswer = int(input("Куда поставим " + PlayerEnt+"? "))
        if PlayerAnswer >= 1 and PlayerAnswer <= 9:
            if (str(board[PlayerAnswer-1]) not in "XO"):
                board[PlayerAnswer-1] = PlayerEnt
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def WinCheck(board):
    """Проверят выигрыш или ничью"""
    win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


count = 0
win = False
while not win:
    PrintBoard(board)
    if count % 2 == 0:
        PlayerInput("X")
    else:
        PlayerInput("O")
    count += 1
    if count > 4:
        tmp = WinCheck(board)
        if tmp:
            print(tmp, "Выиграл!")
            win = True
            break
    if count == 9:
        print("Ничья!")
        break
PrintBoard(board)
