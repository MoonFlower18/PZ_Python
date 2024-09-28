print("Для начала введём несколько требуемых переменных...")

def z1():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    l1 = []

    for i1 in a:
        if i1 < 5:
            l1.append(i1)
    return l1

def z2():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    l2 = list(set(a) & set(b))
    return l2

def z3():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l3 = []
    i3 = 0

    for k in a:
        s = i3 + k
        l3.append(s)
        i3 = k
    return s

def z4():
    a4 = int(input("Для задачи №4 введите целое число: "))
    b = a4 + a4 * a4 + a4 * a4 * a4
    return b

def z5():
    import os
    l5 = []
    dir = r'C:\<directory>\PZ_1' # тут нужен свой путь
    f = os.listdir(dir)
    for i5 in f:
        r5 = dir+"//"+i5
        if os.path.isfile(r5):
            l5.append(i5)
    return l5[0:3] #для вывода первых 3-х файлов, чтобы не ломало таблицу, можно настроить своё количество

def z6():
    n = input("Для задачи №6 введите целое число: ")
    sum = 0

    for i6 in n:
        if i6.isdigit():
            sum += int(i6)
    return sum

from prettytable import PrettyTable

rez = PrettyTable()
rez.field_names = ["Номер задачи", "Результаты работы программ"]
rez.align["Номер задачи"] = "с"
rez.align["Результаты работы программ"] = "l"

rez.add_row(["Задача №1", "Все элементы, которые меньше 5: " + ", ".join(map(str, z1()))], divider=True)
rez.add_row(["Задача №2", "Список из элементов, общих для 2-х списков: " + ", ".join(map(str, z2()))], divider=True)
rez.add_row(["Задача №3", "Сумма предыдущего и текущего числа из первых 10 цифр: " + str(z3())], divider=True)
rez.add_row(["Задача №4", "Итог вычисления по формуле n + nn + nnn: " + str(z4())], divider=True)
rez.add_row(["Задача №5", "Первые 3 файла в заданной директории: " + str(z5())], divider=True)
rez.add_row(["Задача №6", "Сумма чисел заданного числа: " + str(z6())], divider=True)

print("\nИтоговая таблица:")
print(rez)