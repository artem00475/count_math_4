def linear(n, x_table, y_table):
    sx = sum(x_table)
    sy = sum(y_table)
    sxx = 0
    for i in x_table:
        sxx += i**2
    sxy = 0
    for i in range(n):
        sxy += x_table[i]*y_table[i]
    a = round((sxy*n-sx*sy)/(sxx*n-sx*sx), 5)
    b = round((sxx*sy-sx*sxy)/(sxx*n-sx*sx), 5)
    print(a, b)
    p_table = []
    e_table = []
    for i in range(n):
        p_table.append(round(a*x_table[i]+b, 5))
        e_table.append(round(p_table[i]-y_table[i], 5))
    return p_table, e_table


def quadratic(n, x_table, y_table):
    sx = sum(x_table)
    sy = sum(y_table)
    sxx = 0
    for i in x_table:
        sxx += i ** 2
    sxxx = 0
    for i in x_table:
        sxxx += i ** 3
    sxxxx = 0
    for i in x_table:
        sxxxx += i ** 4
    sxy = 0
    for i in range(n):
        sxy += x_table[i] * y_table[i]
    sxxy = 0
    for i in range(n):
        sxxy += x_table[i] ** 2 * y_table[i]
    table = [[n, sx, sxx, sy], [sx, sxx, sxxx, sxy], [sxx, sxxx, sxxxx, sxxy]]
    a_table = calculate_matrix(table, 3)
    print(a_table)
    p_table = []
    e_table = []
    for i in range(n):
        p_table.append(round(a_table[0]+a_table[1]*x_table[i]+a_table[2]*x_table[i]**2, 5))
        e_table.append(round(p_table[i] - y_table[i], 5))
    return p_table, e_table


def third(n, x_table, y_table):
    sx = sum(x_table)
    sy = sum(y_table)
    sxx = 0
    for i in x_table:
        sxx += i ** 2
    sxxx = 0
    for i in x_table:
        sxxx += i ** 3
    sxxxx = 0
    for i in x_table:
        sxxxx += i ** 4
    sxxxxx = 0
    for i in x_table:
        sxxxxx += i ** 5
    sxxxxxx = 0
    for i in x_table:
        sxxxxxx += i ** 6
    sxy = 0
    for i in range(n):
        sxy += x_table[i] * y_table[i]
    sxxy = 0
    for i in range(n):
        sxxy += x_table[i] ** 2 * y_table[i]
    sxxxy = 0
    for i in range(n):
        sxxxy += x_table[i] ** 3 * y_table[i]
    table = [[n, sx, sxx, sxxx, sy], [sx, sxx, sxxx, sxxxx, sxy], [sxx, sxxx, sxxxx, sxxxxx, sxxy], [sxxx, sxxxx, sxxxxx, sxxxxxx, sxxxy]]
    a_table = calculate_matrix(table, 4)
    print(a_table)
    p_table = []
    e_table = []
    for i in range(n):
        p_table.append(round(a_table[0]+a_table[1]*x_table[i]+a_table[2]*x_table[i]**2+a_table[3]*x_table[i]**3, 5))
        e_table.append(round(p_table[i] - y_table[i], 5))
    return p_table, e_table


# Приведение матрицы к треугольному виду с выбором главного элемента по столбцу
def matrix_to_triangle(table, size):
    k = 0
    #Итерация по столбцам
    for column in range(size - 1):
        max_el = 0
        max_row = column
        #print("Выбор главного элемента по", column + 1, "столбцу")
        #Выбор макимального элемента в столбце
        for row in range(column, size):
            if abs(table[row][column]) > max_el:
                max_el = abs(table[row][column])
                max_row = row
        #Перестановка, если необходима
        if max_row != column:
            k += 1
            #print("Меняем местами", max_row+1, "строчку с", column+1, "строкой")
            table1 = table[max_row]
            table[max_row] = table[column]
            table[column] = table1
        #Приведение остальных элементов столбца к нулю
        for row in range(column + 1, size):
            if table[row][column] != 0:
                x = -(table[row][column] / table[column][column])
                table1 = [y * x for y in table[column]]
                for i in range(column, size + 1):
                    table[row][i] = round(table1[i] + table[row][i], 5)
        #print()
    return table, k


# Решение СЛАУ
def calculate_matrix(table, size):
    table1 = table.copy()
    table, replace_count = matrix_to_triangle(table, size)
    #Вектор неизвестных
    x_table = [0 for i in range(size)]
    #Обратный ход метода Гаусса
    for row in range(size - 1, -1, -1):
        sum = table[row][-1]
        for i in range(row + 1, size):
            sum -= table[row][i] * x_table[i]
        x_table[row] = round(sum / table[row][row], 5)
        if abs(x_table[row]) == 0:
            x_table[row] = abs(x_table[row])
    return x_table

