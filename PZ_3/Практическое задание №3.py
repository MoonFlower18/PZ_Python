from tkinter import *
from tkinter import ttk

import psutil

root = Tk()
root.title("Практические задачи")
root.geometry("500x500")

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

def on_combobox_change(event):
    selected_task = tasks_var.get()
    label.config(text="")  # Очищаем текст перед новой операцией
    if selected_task == "Задание №1":
        z1()

    # Здесь вы можете добавить условия для других заданий
    # elif selected_task == "Задание №2":
    #     z2(label1)
    # и так далее...

combobox.bind("<<ComboboxSelected>>", on_combobox_change)

# Инициализируем функцию для задания по умолчанию
on_combobox_change(None)

root.mainloop()