# Вывод таблицы с итерациями в файл
def print_table_to_file(x, y, p, e, f):
    b = [x, y, p, e]
    a = [' x  ', ' y  ', 'P(x)', ' e  ']
    for i in range(4):
        f.write(a[i] + ' ')
        for c in b[i]:
            f.write('%.5f ' % c)
        f.write('\n')


# Вывод результата в файл
def print_to_file(x, y, p, e, dev, s, k):
    name = input("Введите имя файла: ")
    f = open(name, 'w')
    f.write("Среднеквадратичное отклонение: " + str(dev) + '\n')
    f.write("Мера отклонения: " + str(s) + '\n')
    if len(k) == 2:
        f.write("Коэффиценты апроксимирующей фукнции: a = " + str(k[0]) + " b = " + str(k[1]) + '\n')
    elif len(k) == 3:
        f.write("Коэффиценты апроксимирующей фукнции: a = " + str(k[2]) + " b = " + str(k[1]) + " c = " + str(k[0]) + '\n')
    else:
        f.write("Коэффиценты апроксимирующей фукнции: a = " + str(k[3]) + " b = " + str(k[2]) + " c = " + str(k[1]) + " d = " + str(k[0]) + '\n')
    print_table_to_file(x, y, p, e, f)
    f.close()
