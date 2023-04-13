def print_table(x, y, p, e):
    b = [x, y, p, e]
    a = [' x  ', ' y  ', 'P(x)', ' e  ']
    for i in range(4):
        print(a[i], end=' ')
        for c in b[i]:
            print('%.5f' % c, end=' ')
        print()


# Вывод результата в поток вывода
def print_to_output(x, y, p, e, dev, s, k):
    print("Среднеквадратичное отклонение:", dev)
    print("Мера отклонения:", s)
    if len(k) == 2:
        print("Коэффиценты апроксимирующей фукнции: a =", k[0], "b =", k[1])
    elif len(k) == 3:
        print("Коэффиценты апроксимирующей фукнции: a =", k[2], "b =", k[1], "c =", k[0])
    else:
        print("Коэффиценты апроксимирующей фукнции: a =", k[3], "b =", k[2], "c =", k[1], "d =", k[0])
    print_table(x, y, p, e)
