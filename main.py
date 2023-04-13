# Считывание размерности матрицы
from aproximation import linear, quadratic, third, power, exponential, logarithmic
from console_utils import print_to_output
from file_utils import print_to_file


def get_matrix_size():
    print("Количество точек функции (введите f для ввода из файла, k для ввода с клавиатуры:")

    while True:
        input_type = input()
        #Ввод из файла
        if input_type == "f":
            print("В файле должно быть целое число от 8 до 12.")
            while True:
                print("Введите имя файла:")
                file_name = input()
                try:
                    file = open(file_name, 'r')
                    size = int(file.readline())
                    if size < 8 or size > 12:
                        print("Значение должно быть в промежутке [8,12]")
                        continue
                    return size
                except FileNotFoundError:
                    print("Файл не найден. Попробуйте еще раз.")
                    continue
                except ValueError:
                    print("Некорректное значение. Повторите ввод.")
                    continue
        #Ввод с клавиатуры
        elif input_type == "k":
            while True:
                print("Введите целое число от 8 до 12:")
                try:
                    size_string = input()
                    size = int(size_string)
                    if size < 8 or size > 12:
                        print("Значение должно быть в промежутке [8,12]")
                        continue
                    return size
                except ValueError:
                    print("Некорректное значение. Повторите ввод.")
                    continue
        else:
            print("Некорректный формат ввода. Повторите еще раз:")


# Считывание элементов матрицы
def get_matrix_values(size):
    print("Точки (введите f для ввода из файла, k для ввода с клавиатуры:")

    while True:
        input_type = input()
        #Ввод из файла
        if input_type == "f":
            print(
                "Данные в файле должны быть в формате каждая пара в отдельной строке файла, элементы в строке разделяются пробелами.")
            while True:
                print("Введите имя файла:")
                file_name = input()
                try:
                    file = open(file_name, 'r')
                    table = [['   x   ', '   y   ']]
                    for row in range(size):
                        elements_string = file.readline().split()
                        if len(elements_string) != 2:
                            print("Неправильное количество элементов в строке", row + 1)
                            raise ArithmeticError
                        table.append(list(map(float, elements_string)))
                    return table
                except FileNotFoundError:
                    print("Файл не найден. Попробуйте еще раз.")
                    continue
                except ValueError:
                    print("Некорректные значения. Повторите ввод.")
                    continue
                except ArithmeticError:
                    continue
        #Ввод с клавиатуры
        elif input_type == "k":
            while True:
                table = [['   x   ', '   y   ']]
                for row in range(size):
                    while True:
                        print("Введите координаты ", row + 1, " точки через пробел:")
                        try:
                            elements_string = input().split()
                            if len(elements_string) != 2:
                                print("Неправильное количество элементов в строке")
                                continue
                            table.append(list(map(float, elements_string)))
                            break
                        except ValueError:
                            print("Некорректные значения. Повторите ввод.")
                            continue
                return table
        else:
            print("Некорректный формат ввода. Повторите еще раз:")


# Вывод результата
def print_result(table, x, count, fx):
    while True:
        t = input("Для вывода в консоль введите c, для сохранения в файл введите f: ")
        if t.split()[0] == "f":
            print_to_file(table, x, count, fx)
            break
        elif t.split()[0] == "c":
            print_to_output(table, x, count, fx)
            break
        else:
            print("Повторите ввод")


def print_table(x, y, p, e):
    b = [x, y, p, e]
    a = [' x  ', ' y  ', 'P(x)', ' e  ']
    for i in range(4):
        print(a[i], end=' ')
        for c in b[i]:
            print('%.5f' % c, end=' ')
        print()


print("Апроксимация фукнции.")
matrix_size = get_matrix_size()
print("Количество точек - ", matrix_size)
table = get_matrix_values(matrix_size)
print("\nВведенная таблица")
print_to_output(table)
print()
x_table = []
y_table = []
for i in range(1, len(table)):
    x_table.append(table[i][0])
    y_table.append(table[i][1])
#линейная
p_table, e_table, deviation, s = linear(matrix_size, x_table, y_table)
print_table(x_table, y_table, p_table, e_table)
print(deviation, s)
print()
#квадратичная
p_table, e_table, deviation, s = quadratic(matrix_size, x_table, y_table)
print_table(x_table, y_table, p_table, e_table)
print(deviation, s)
print()
#3 степень
p_table, e_table, deviation, s = third(matrix_size, x_table, y_table)
print_table(x_table, y_table, p_table, e_table)
print(deviation, s)
print()
if float(min(x_table)) > 0 and float(min(y_table)) > 0:
    #степенная
    p_table, e_table, deviation, s = power(matrix_size, x_table, y_table)
    print_table(x_table, y_table, p_table, e_table)
    print(deviation, s)
    print()
if float(min(y_table)) > 0:
    #степенная
    p_table, e_table, deviation, s = exponential(matrix_size, x_table, y_table)
    print_table(x_table, y_table, p_table, e_table)
    print(deviation, s)
    print()
if float(min(x_table)) > 0:
    #степенная
    p_table, e_table, deviation, s = logarithmic(matrix_size, x_table, y_table)
    print_table(x_table, y_table, p_table, e_table)
    print(deviation, s)
    print()
