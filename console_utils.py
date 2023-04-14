def print_table(x, y, p, e):
    b = [x, y, p, e]
    a = [' x  ', ' y  ', 'P(x)', ' e  ']
    for i in range(4):
        print(a[i], end=' ')
        for c in b[i]:
            print('%.5f' % c, end=' ')
        print()


def print_table_res(table):
    for c in table[0]:
        print(c, end='    ')
    print()
    for row in table[1:]:
        count = 0
        for c in row:
            if count == 0:
                print(c, end='    ')
                count += 1
            else:
                if c >= 0:
                    print(' %.5f' % c, end='    ')
                else:
                    print('%.5f' % c, end='    ')
        print()


# Вывод результата в поток вывода
def print_to_output(x, y, p, e, dev, s, k, table, cor, text):
    print("Результаты аппрокссимации:")
    print_table_res(table)
    print("Коэффициент корреляции Пирсона:", round(cor, 6), '\n')
    print(text)
    print("Среднеквадратичное отклонение:", round(dev, 6))
    print("Мера отклонения:", round(s, 6))
    if len(k) == 2:
        print("Коэффиценты апроксимирующей фукнции: a =", k[0], "b =", k[1])
    elif len(k) == 3:
        print("Коэффиценты апроксимирующей фукнции: a =", k[2], "b =", k[1], "c =", k[0])
    else:
        print("Коэффиценты апроксимирующей фукнции: a =", k[3], "b =", k[2], "c =", k[1], "d =", k[0])
    print_table(x, y, p, e)
