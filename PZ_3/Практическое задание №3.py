from tkinter import *
from tkinter import ttk
from tkinter import messagebox, scrolledtext
import tkinter as tk

import psutil

root = Tk()
root.title("Практические задачи")
root.geometry("500x600+530+100")

tasks = [" - выберите задачу - ", "Задание №1", "Задание №2", "Задание №3", "Задание №4", "Задание №5"]
tasks_var = StringVar(value=tasks[0])

combobox = ttk.Combobox(textvariable=tasks_var, values=tasks, state="readonly")
combobox.pack(anchor=NW, padx=6, pady=6)

frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[5, 5])
frame.pack(anchor=NW, padx=5, pady=1)

label = ttk.Label(frame)
label.pack()


def z1():
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

    label.config(text=output)


def z2():
    import os
    os.chdir(r"C:\Users\Юлия\Downloads\PZ_Python\PZ_3")
    # try:
    #     os.path.exists(r"E:\Программы\Проекты Питон\PZ_3\first.txt")
    # except False:
    #     print("21212")

    # =============================== создание файла ================================ #

    file_name_var = tk.StringVar()

    create_frame = ttk.Frame()
    create_frame.pack(pady=10)

    def create_file():
        file_name = file_name_var.get() + ".txt"
        if file_name:
            with open(file_name, 'w') as f:
                f.write("")
            messagebox.showinfo("Успех", f"Файл '{file_name}' создан.")
        else:
            messagebox.showwarning("Ошибка", "Введите название файла.")

    ttk.Label(create_frame, text="Название файла:").pack(side=tk.LEFT, ipadx=1)
    ttk.Entry(create_frame, textvariable=file_name_var).pack(side=tk.LEFT)
    ttk.Button(create_frame, text="Создать файл", command=create_file).pack(side=tk.LEFT, padx=5)

    # ============================ отображение содержимого ============================ #

    content_frame = ttk.Frame()
    content_frame.pack(pady=10)

    def display_content():
        file_name = file_name_var.get() + ".txt"

        if os.path.exists(file_name):
            with open(file_name, 'r', encoding="utf-8") as f:
                content = f.read()
            content_area.config(state=tk.NORMAL)  # разрешаем редактирование временно
            content_area.delete('1.0', tk.END)  # очищаем область
            content_area.insert(tk.INSERT, content)  # вставляем текст
            content_area.config(state=tk.DISABLED)  # запрещаем редактирование
        else:
            messagebox.showwarning("Ошибка", "Файл не существует.")

    tk.Label(content_frame, text="Содержимое документа:").pack(pady=3)

    content_area = scrolledtext.ScrolledText(content_frame, width=30, height=10, state=tk.DISABLED)  # состояние
    # изначально отключено
    content_area.pack()

    tk.Button(content_frame, text="Отобразить содержимое файла", command=display_content).pack(pady=5)

    # ============================ добавление текста ============================ #

    add_line_frame = tk.Frame()
    add_line_frame.pack(pady=10)

    def add_line():
        file_name = file_name_var.get() + ".txt"
        line_to_add = text_area.get("1.0", tk.END).strip()  # получаем весь текст из text_area
        if os.path.exists(file_name) and line_to_add:
            with open(file_name, 'a', encoding="utf-8") as f:
                f.write("\n" + line_to_add)
            messagebox.showinfo("Успех", "Строка добавлена в файл.")
            text_area.delete("1.0", tk.END)  # Очищаем text_area
        else:
            messagebox.showwarning("Ошибка", "Файл не существует или строка пуста.")

    tk.Label(add_line_frame, text="Строка для добавления:").pack(pady=3)

    # Создаем многострочное текстовое поле
    text_area = scrolledtext.ScrolledText(add_line_frame, wrap=tk.WORD, width=30, height=5)
    text_area.pack()

    tk.Button(add_line_frame, text="Добавить в файл", command=add_line).pack(pady=5)

    # ============================ удаление текста ============================ #

    delete_frame = tk.Frame()
    delete_frame.pack(pady=10)

    def delete_file():
        file_name = file_name_var.get() + ".txt"
        if os.path.exists(file_name):
            os.remove(file_name)
            messagebox.showinfo("Успех", f"Файл '{file_name}' удален.")
        else:
            messagebox.showwarning("Ошибка", "Файл не существует.")

    tk.Label(delete_frame, text="Для удаления файла нажмите на кнопку -> ").pack(pady=5, side=tk.LEFT)
    tk.Button(delete_frame, text="Удалить файл", command=delete_file).pack(pady=10, side=tk.LEFT)


def on_combobox_change(event):
    selected_task = tasks_var.get()
    label.config(text="")
    if selected_task == " - выберите задачу - ":
        frame.pack_forget()
    elif selected_task == "Задание №1":
        frame.pack(anchor=NW, padx=5, pady=1)
        z1()
    elif selected_task == "Задание №2":
        frame.pack_forget()
        z2()


combobox.bind("<<ComboboxSelected>>", on_combobox_change)
on_combobox_change(None)

root.mainloop()
