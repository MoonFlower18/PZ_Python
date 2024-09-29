import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, scrolledtext
import tkinter as tk

import psutil
import os

web = Tk()
web.title("Практические задачи")
web.geometry("500x600+530+100")

ttk.Label(text="Выбранная задача: ").pack(anchor=NW, padx=4, pady=1)

tasks = [" - выберите задачу - ", "Задание №1", "Задание №2", "Задание №3"]
tasks_var = StringVar(value=tasks[0])

combobox = ttk.Combobox(textvariable=tasks_var, values=tasks, state="readonly")
combobox.pack(anchor=NW, padx=6, pady=6)

# фрейм для задач
task_frame = Frame(web)
task_frame.pack(anchor=NW, fill=BOTH)


def clear_task_frame():
    # удаление всех деталей из фрейма с задачами
    for widget in task_frame.winfo_children():
        widget.destroy()


def z1():
    clear_task_frame()

    frame1 = ttk.Frame(task_frame, borderwidth=3, relief=RIDGE, padding=[5, 5])
    frame1.pack(anchor=NW, padx=5, pady=1)

    label_z1 = ttk.Label(frame1)
    label_z1.pack()

    output = ""

    parts = psutil.disk_partitions()
    output += "Информация о дисках системы: \n+-------------------------------------+"

    for part in parts:
        try:
            part_usage = psutil.disk_usage(part.mountpoint)
            output += (f"\nИмя логического диска: {part.device}\n"
                       f"Метка тома: {part.mountpoint}\n"
                       f"Тип файловой системы: {part.fstype}\n"
                       f"Размер файловой системы: {part_usage.total / (1024 ** 3):.0f} ГБ\n")
        except PermissionError:
            output += "\nНе хватает прав для доступа к информации о диске.\n"

        output += "+-------------------------------------+"

    label_z1.config(text=output)


def z2():
    clear_task_frame()

    os.chdir(r"C:\Users\Юлия\Downloads\PZ_Python\PZ_3")

    # =============================== создание файла ================================ #

    file_name_var = tk.StringVar()

    create_frame = ttk.Frame(task_frame)
    create_frame.pack(pady=10)

    def create_file():
        file_name = file_name_var.get() + ".txt"
        if not file_name_var.get():  # проверка на пустую строку
            messagebox.showwarning("Ошибка", "Введите название файла.")
            return
        try:
            if os.path.exists(file_name):
                raise FileExistsError()  # raise для принудительного вызова ошибки

            with open(file_name, 'w') as f:
                f.write("")
            messagebox.showinfo("Успех", f"Файл '{file_name}' создан.")

        except FileExistsError:
            messagebox.showerror("Ошибка", "Файл уже создан.")
        except OSError:  # на случай запрещённых символов в названии \ / * ? " < > |
            messagebox.showerror("Ошибка", "Произошла ошибка при создании файла.")

    ttk.Label(create_frame, text="Название файла:").pack(side=tk.LEFT, ipadx=1)
    ttk.Entry(create_frame, textvariable=file_name_var).pack(side=tk.LEFT)
    ttk.Button(create_frame, text="Создать файл", command=create_file).pack(side=tk.LEFT, padx=5)

    # ============================ отображение содержимого ============================ #

    content_frame = ttk.Frame(task_frame)
    content_frame.pack(pady=10)

    def display_content():
        file_name = file_name_var.get() + ".txt"

        try:
            if not os.path.exists(file_name):
                raise FileNotFoundError()

            with open(file_name, 'r', encoding="utf-8") as f:
                content = f.read()
            content_area.config(state=tk.NORMAL)  # разрешение на временный редакт поля
            content_area.delete('1.0', tk.END)  # чистка старых данных
            content_area.insert(tk.INSERT, content)  # вставка нового текста
            content_area.config(state=tk.DISABLED)  # закрываем редакт поля
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файла не существует.")

    tk.Label(content_frame, text="Содержимое документа:").pack(pady=3)

    content_area = scrolledtext.ScrolledText(content_frame, width=30, height=10)
    content_area.pack()

    tk.Button(content_frame, text="Отобразить содержимое файла", command=display_content).pack(pady=5)

    # ============================ добавление текста ============================ #

    add_line_frame = tk.Frame(task_frame)
    add_line_frame.pack(pady=10)

    def add_line():
        file_name = file_name_var.get() + ".txt"
        line_to_add = text_area.get("1.0", tk.END).strip()  # получение всего текста из text_area

        try:
            if not os.path.exists(file_name):
                raise FileNotFoundError()

            if not line_to_add:  # проверка на пустую строку
                messagebox.showwarning("Ошибка", "Пустая строка. Пожалуйста, введите данные.")
                return

            with open(file_name, 'a', encoding="utf-8") as f:
                f.write("\n" + line_to_add)
            messagebox.showinfo("Успех", "Строка добавлена в файл.")
            text_area.delete("1.0", tk.END)  # чистка text_area для нового ввода

        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файла не существует.")

    tk.Label(add_line_frame, text="Строка для добавления:").pack(pady=3)

    # многострочное текстовое поле
    text_area = scrolledtext.ScrolledText(add_line_frame, wrap=tk.WORD, width=30, height=5)
    text_area.pack()

    tk.Button(add_line_frame, text="Добавить в файл", command=add_line).pack(pady=5)

    # ============================ удаление текста ============================ #

    delete_frame = tk.Frame(task_frame)
    delete_frame.pack(pady=10)

    def delete_file():
        file_name = file_name_var.get() + ".txt"

        try:
            if not os.path.exists(file_name):
                raise FileNotFoundError()
            os.remove(file_name)
            messagebox.showinfo("Успех", f"Файл '{file_name}' удален.")

        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файла не существует.")

    tk.Label(delete_frame, text="Для удаления файла нажмите на кнопку -> ").pack(pady=5, side=tk.LEFT)
    tk.Button(delete_frame, text="Удалить файл", command=delete_file).pack(pady=10, side=tk.LEFT)















def z3():
    clear_task_frame()

    os.chdir(r"C:\Users\Юлия\Downloads\PZ_Python\PZ_3")

    # =============================== создание файла ================================ #

    file_name_var_z3 = tk.StringVar()

    create_frame_z3 = ttk.Frame(task_frame)
    create_frame_z3.pack(pady=10)

    def create_file_z3():
        file_name_z3 = file_name_var_z3.get() + ".json"
        if not file_name_var_z3.get():  # проверка на пустую строку
            messagebox.showwarning("Ошибка", "Введите название файла.")
            return
        try:
            if os.path.exists(file_name_z3):
                raise FileExistsError()  # raise для принудительного вызова ошибки

            with open(file_name_z3, 'w') as f:
                f.write("")
            messagebox.showinfo("Успех", f"Файл '{file_name_z3}' создан.")

        except FileExistsError:
            messagebox.showerror("Ошибка", "Файл уже создан.")
        except OSError:  # на случай запрещённых символов в названии \ / * ? " < > |
            messagebox.showerror("Ошибка", "Произошла ошибка при создании файла.")

    ttk.Label(create_frame_z3, text="Название файла:").pack(side=tk.LEFT, ipadx=1)
    ttk.Entry(create_frame_z3, textvariable=file_name_var_z3).pack(side=tk.LEFT)
    ttk.Button(create_frame_z3, text="Создать файл", command=create_file_z3).pack(padx=5, side=tk.LEFT)

    # ============================ отображение содержимого ============================ #

    content_frame_z3 = ttk.Frame(task_frame)
    content_frame_z3.pack(pady=10)

    def display_content_z3():
        file_name_z3 = file_name_var_z3.get() + ".json"

        try:
            if not os.path.exists(file_name_z3):
                raise FileNotFoundError()

            with open(file_name_z3, encoding='utf-8') as f:
                content_z3 = json.load(f)
            content_area_z3.config(state=tk.NORMAL)  # разрешение на временный редакт поля
            content_area_z3.delete('1.0', tk.END)  # чистка старых данных
            content_area_z3.insert(tk.INSERT, json.dumps(content_z3, ensure_ascii=False, indent=4)) # вставка нового текста
            content_area_z3.config(state=tk.DISABLED)  # закрываем редакт поля
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файла не существует.")
        except json.JSONDecodeError:
            messagebox.showerror("Ошибка", "Ошибка чтения файла JSON.")

    tk.Label(content_frame_z3, text="Содержимое документа:").pack(pady=3)

    content_area_z3 = scrolledtext.ScrolledText(content_frame_z3, width=30, height=10)
    content_area_z3.pack()

    tk.Button(content_frame_z3, text="Отобразить содержимое файла", command=display_content_z3).pack(pady=5)

    # ============================ добавление текста ============================ #

    add_lines_frame = tk.Frame(task_frame)
    add_lines_frame.pack(pady=10)

    def add_lines_z3():
        file_name_z3 = file_name_var_z3.get() + ".json"

        try:
            if not os.path.exists(file_name_z3):
                raise FileNotFoundError()

            with open(file_name_z3, 'r', encoding='utf-8') as j:
                if os.path.getsize(file_name_z3) == 0:  # проверка на пустой файл
                    ex_data = []  # создадим новый список, чтобы не было ошибки json.JSONDecodeError
                else:
                    ex_data = json.load(j)

                if isinstance(ex_data, dict):
                    # Конвертация словаря в список
                    ex_data = list(ex_data.values())
                elif not isinstance(ex_data, list):
                    raise ValueError("Данные в файле должны быть либо списком, либо объектом.")

            if fam.get().isalpha() and name.get().isalpha() and (och.get().isalpha() or och.get() == ""):
                fio = {
                    "Фамилия": fam.get(),
                    "Имя": name.get(),
                    "Отчество": och.get()
                }
            else:
                messagebox.showerror("Ошибка", "ФИО должно состоять из букв.")


            ex_data.append(fio)

            with open(file_name_z3, 'w', encoding='utf-8') as j:
                json.dump(ex_data, j, ensure_ascii=False, indent=4)

            messagebox.showinfo("Успех", "Данные успешно записаны в файл.")

        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файла не существует.")
        except TypeError:
            messagebox.showerror("Ошибка", "Некорректный ввод данных.")
        except json.JSONDecodeError:
            messagebox.showerror("Ошибка", "Ошибка чтения файла JSON. Неверный формат.")

    tk.Label(add_lines_frame, text="Введите ФИО абитуриента: ").pack(pady=3)

    fam_frame = tk.Frame(add_lines_frame)
    fam_frame.pack(pady=1)

    name_frame = tk.Frame(add_lines_frame)
    name_frame.pack(pady=1)

    och_frame = tk.Frame(add_lines_frame)
    och_frame.pack(pady=1)

    tk.Label(fam_frame, text="Фамилия: ").pack(pady=3, side=tk.LEFT)
    fam = ttk.Entry(fam_frame)
    fam.pack(anchor=NW, padx=6, pady=6, side=tk.LEFT)

    tk.Label(name_frame, text="Имя: ").pack(pady=3, side=tk.LEFT)
    name = ttk.Entry(name_frame)
    name.pack(anchor=NW, padx=6, pady=6, side=tk.LEFT)

    tk.Label(och_frame, text="Отчество: ").pack(pady=3, side=tk.LEFT)
    och = ttk.Entry(och_frame)
    och.pack(anchor=NW, padx=6, pady=6, side=tk.LEFT)

    tk.Button(add_lines_frame, text="Добавить в файл", command=add_lines_z3).pack(pady=5)


    # ============================ удаление текста ============================ #

    delete_frame_z3 = tk.Frame(task_frame)
    delete_frame_z3.pack(pady=10)

    def delete_file_z3():
        file_name_z3 = file_name_var_z3.get() + ".json"

        try:
            if not os.path.exists(file_name_z3):
                raise FileNotFoundError()
            os.remove(file_name_z3)
            messagebox.showinfo("Успех", f"Файл '{file_name_z3}' удален.")

        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файла не существует.")

    tk.Label(delete_frame_z3, text="Для удаления файла нажмите на кнопку -> ").pack(pady=5, side=tk.LEFT)
    tk.Button(delete_frame_z3, text="Удалить файл", command=delete_file_z3).pack(pady=10, side=tk.LEFT)


def on_combobox_change(event):
    selected_task = tasks_var.get()
    if selected_task == "Задание №1":
        z1()
    elif selected_task == "Задание №2":
        z2()
    elif selected_task == "Задание №3":
        z3()
    else:
        clear_task_frame()  # чистка фреймов, если выбрано " - выберите задачу - "


combobox.bind("<<ComboboxSelected>>", on_combobox_change)
on_combobox_change(None)

web.mainloop()
