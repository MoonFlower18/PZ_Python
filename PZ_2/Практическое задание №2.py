# для 1 задачи
import random
import datetime

# для 2 задачи
import re
from playsound import playsound

# для 3-5 задачи
# import re
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def z1():
    def decor(func):
        def modif():
            print("Текущая дата и время: ", datetime.datetime.now(), "\n=================================================")
            func()
            print("=================================================\nДата и время после выполнения функции: ", datetime.datetime.now())

        return modif

    @decor
    def print_t():
        b = int(input("Введите число от 10 млн до 15 млн: "))
        a = 0
        while a != b:
            a = random.randint(1, 15000000)
        print("Найдено совпадение чисел!")

    print_t()


def z2():
    tel = input("Введите номер телефона из 10 цифр в формате 00хххххххх: ")

    while (len(tel) != 10) or not re.match(r'^00[0-9]{8}$', tel):
        playsound(r"C:\Users\Yuliya\Desktop\ban.mp3")
        print("Ошибка! Некорректный ввод номера телефона!")
        tel = input("Введите корректный номер телефона из 10 цифр в формате 00хххххххх: ")

    print("Отформатированный номер телефона:", re.sub(r'^00', '+', tel))

def z3():
    def check():
        word = entry.get()

        if len(word) == 4:
            if re.match(r'^m[a-zA-z]{2}e$', word):  # проверка м с начала, 2 любые буквы и е в конце
                messagebox.showinfo("Result", "Match!")
            else:
                messagebox.showerror("Error", "No match!")
        else:
            messagebox.showwarning("Warning", "Количество символов в слове ≠ 4!")

    web = Tk()
    web.title("Проверка слова")
    web.geometry("260x100+640+240")  # ширина х высота + отступ слева + отступ сверху
    web.configure(background="#F5F5F5", cursor="diamond_cross")

    entry = ttk.Entry(web)
    entry.pack(anchor="center", pady=15)  # позиция по центру + отступ верх-низ 15

    btn = ttk.Button(web, text="Запустить проверку!", command=check)
    btn.pack(anchor="center")

    web.mainloop()

def z4():
    def check():
        word = entry.get()

        if re.match(r'\w+@[a-zA-Z]+\.[a-zA-Z]+$', word):  # проверка все буквы до @, потом все буквы до экранированной точки и все буквы после
            messagebox.showinfo("Результат", "Это действительно почта!")
        else:
            messagebox.showerror("Ошибка", "Данный адрес не является почтой!")

    web = Tk()
    web.title("Проверка почты")
    web.geometry("260x100+640+240")  # ширина х высота + отступ слева + отступ сверху
    web.configure(background="#F5F5F5", cursor="diamond_cross")

    entry = ttk.Entry(web)
    entry.pack(anchor="center", pady=15)  # позиция по центру + отступ верх-низ 15

    btn = ttk.Button(web, text="Запустить проверку!", command=check)
    btn.pack(anchor="center")

    web.mainloop()

def z5():
    def check():
        word = text_widget.get("1.0", tk.END)  # Получаем текст с первой строки до конца

        find = re.findall(r'\w+@[a-zA-Z]+\.[a-zA-Z]+', word)  # проверка все буквы до @, потом все буквы до экранированной точки и все буквы после
        label["text"] = '\n'.join(find)  # вывод на новые строки

    web = Tk()
    web.title("Проверка почты")
    x = web.winfo_screenwidth()  # размер по горизонтали из размера экрана
    y = web.winfo_screenheight()  # размер по вертикали из размера экрана
    web.geometry('{}x{}+630+250'.format(int(x * 0.3), int(y * 0.4)))  # ширина х высота (умножить на процент) +
    # отступ слева + отступ сверху
    web.configure(background="#F5F5F5", cursor="diamond_cross")

    text1 = ttk.Label(text="Введите исходный текст:", font="system")
    text1.pack(anchor="center", pady=5)

    # фрейм для размещения текстового поля и скроллбара
    frame = ttk.Frame(web)
    frame.pack(padx=10, pady=10)

    # текстовое поле вместо entry для многострочности
    text_widget = tk.Text(frame, width=40, height=5, wrap=tk.WORD)  # wrap=tk.WORD для переноса по словам
    text_widget.pack(side=tk.LEFT)  # выравнивание по левой стороне

    # скроллбар связываем с текстовым полем
    scrollbar = ttk.Scrollbar(frame, command=text_widget.yview)  # Для прокрутки по вертикали прокручиваемый виджет имеет yview
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # выравнивание по левой стороне + растягивание по У

    text_widget.config(yscrollcommand=scrollbar.set)  # у прокручиваемого виджета есть параметр yscrollcommand принимающий вызов метода set объекта scrollbar

    btn = ttk.Button(web, text="Запустить проверку!", command=check)
    btn.pack(anchor="center", pady=5)

    text2 = ttk.Label(text="Список найденных почт:", font="system")
    text2.pack(anchor="center", pady=5)

    label = ttk.Label(web)
    label.pack(anchor="center")

    web.mainloop()

# ============================ вывод ответов ============================ #

choice = int(input("Введите номер задачи или '0' - чтобы завершить выполнение: "))
while choice != 0:
    if choice == 1:
        z1()
        print("Выполнение задачи №1 завершено!\n")
    elif choice == 2:
        z2()
        print("Выполнение задачи №2 завершено!\n")
    elif choice == 3:
        z3()
        print("Выполнение задачи №3 завершено!\n")
    elif choice == 4:
        z4()
        print("Выполнение задачи №4 завершено!\n")
    elif choice == 5:
        z5()
        print("Выполнение задачи №5 завершено!\n")

    choice = int(input("Введите номер задачи или '0' - чтобы завершить выполнение: "))
print("Программа завершена!")