from prettytable import PrettyTable
import random


def win_check(data):
    result = [
        (data[0][0] == data[1][0] == data[2][0] != ""),  # выигрыш по первому столбцу
        (data[0][1] == data[1][1] == data[2][1] != ""),  # выигрыш по второму столбцу
        (data[0][2] == data[1][2] == data[2][2] != ""),  # выигрыш по третьему столбцу
        (data[0][0] == data[0][1] == data[0][2] != ""),  # выигрыш по первой строке
        (data[1][0] == data[1][1] == data[1][2] != ""),  # выигрыш по второй строке
        (data[2][0] == data[2][1] == data[2][2] != ""),  # выигрыш по третьей строке
        (data[0][0] == data[1][1] == data[2][2] != ""),  # выигрыш по правой диагонали
        (data[0][2] == data[1][1] == data[2][0] != "")]  # выигрыш по левой диагонали
    return any(result)


def tic_tac_toe():
    data = [["", "", ""], ["", "", ""], ["", "", ""]]  # список строк таблицы
    player_1 = input("Введите имя первого игрока: "), "x"
    player_2 = input("Введите имя второго игрока: "), "o"
    player = random.choice([player_1, player_2])

    while True:
        output_data = PrettyTable()
        output_data.field_names = [" ", "A", "B", "C"]
        output_data.add_rows([[1, *data[0]],
                              [2, *data[1]],
                              [3, *data[2]]])

        print(output_data)

        user_input = input(f"{player[0]}, введите номер ячейки в формате 'А1' (на английском)"
                           f" или введите '*', чтобы выйти: ")

        if user_input == "*":
            print(f"Игра окончена! {player[0]} сдался")
            break
        try:
            i = ["1", "2", "3"].index(user_input[1:])
            j = ["a", "b", "c"].index(user_input[0].lower())

            if data[i][j]:
                print("Эта клетка уже занята")
                continue

            data[i][j] = player[1]
        except (ValueError, IndexError):
            print("УПС, что-то пошло не так, перепроверьте данные для ввода!")
            continue

        if win_check(data):
            print(output_data)
            print(f"Игра окончена! Поздравляем {player[0]}, вы победили!")
            break

        if all(all(item) for item in data):
            print(output_data)
            print("Игра окончена! Ничья!")
            break

        player = player_1 if player == player_2 else player_2


if __name__ == "__main__":
    tic_tac_toe()
