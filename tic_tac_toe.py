# Tic Tac Toe Game in Python

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}   1 | 2 | 3")  # Вывод верхней строки доски и номеров позиций
    print("- + - + -")                                           # Вывод разделительной линии
    print(f"{board[3]} | {board[4]} | {board[5]}   4 | 5 | 6")  # Вывод средней строки доски и номеров позиций
    print("- + - + -")                                           # Вывод разделительной линии
    print(f"{board[6]} | {board[7]} | {board[8]}   7 | 8 | 9")  # Вывод нижней строки доски и номеров позиций


def check_win(board, player):
    win_combinations = [                                          # Список выигрышных комбинаций
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтали             # горизонтальные линии
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикали               # вертикальные линии
        [0, 4, 8], [2, 4, 6]              # диагонали               # диагональные линии
    ]
    for combo in win_combinations:                                 # Перебор всех комбинаций
        if all(board[cell] == player for cell in combo):           # Проверка, что все клетки в комбинации заняты игроком
            return True                                            # Если условие выполняется, возвращаем True
    return False                                                   # Если ни одна комбинация не выиграла, возвращаем False


def check_draw(board):
    return all(cell != ' ' for cell in board)                      # Проверка на ничью: если все клетки заняты ('X' или 'O'), возвращаем True


def main():
    board = [' '] * 9  # Инициализация пустого игрового поля       # Создание списка из 9 пустых клеток (доска)
    current_player = 'X'  # Игрок, который начинает игру           # Установка начального игрока

    print_board(board)  # Вывод начального состояния игрового поля  # Вывод начального состояния доски перед началом игры

    while True:                                                     # Бесконечный цикл игры
        position = int(input(f"Игрок {current_player}, введите ваш ход (1-9): ")) - 1  # Ввод позиции хода от игрока (1-9)

        if board[position] == ' ':                                  # Проверка, что выбранная позиция на доске пустая
            board[position] = current_player                        # Установка символа текущего игрока на доске

            if check_win(board, current_player):                    # Проверка на выигрыш текущего игрока
                print_board(board)                                  # Вывод текущего состояния доски
                print(f"Поздравляем! Игрок {current_player} победил!")  # Вывод сообщения о победе текущего игрока
                break                                               # Выход из цикла, завершение игры
            elif check_draw(board):                                 # Проверка на ничью
                print_board(board)                                  # Вывод текущего состояния доски
                print("Ничья!")                                     # Вывод сообщения о ничьей
                break                                               # Выход из цикла, завершение игры
            else:
                # Смена игрока                                      # Переключение на другого игрока для следующего хода
                current_player = 'O' if current_player == 'X' else 'X'
            
            # Очистка экрана перед выводом обновленного состояния доски
            print("\033[H\033[J")                                   # ANSI escape коды для очистки экрана консоли
            print_board(board)                                      # Вывод обновленного состояния доски
        else:
            print("Эта позиция уже занята. Пожалуйста, выберите другую.")  # Вывод сообщения об ошибке, если позиция уже занята


if __name__ == "__main__":
    main()  # Вызов основной функции игры при запуске скрипта
