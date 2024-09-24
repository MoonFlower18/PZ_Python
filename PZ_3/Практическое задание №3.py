from tkinter import *
from tkinter import ttk

import psutil

root = Tk()
root.title("Практические задачи")
root.geometry("500x500")

tasks = ["Задание №1", "Задание №2", "Задание №3", "Задание №4", "Задание №5"]
tasks_var = StringVar(value=tasks[0])

combobox = ttk.Combobox(textvariable=tasks_var, values=tasks, state="readonly")
combobox.pack(anchor=NW, padx=6, pady=6)


def z1(label):
    output = ""

    parts = psutil.disk_partitions()
    output += "+-------------------------------------+"

    for part in parts:
        try:
            part_usage = psutil.disk_usage(part.mountpoint)
            output += (f"\nИмя логического диска: {part.device}\n"
                       f"Метка тома: {part.mountpoint}\n"
                       f"Тип файловой системы: {part.fstype}\n"
                       f"Размер файловой системы: {part_usage.total / (1024 ** 3):.0f} ГБ\n")
        except PermissionError:
            output += "Не хватает прав для доступа к информации о диске.\n"

        output += "+-------------------------------------+"

    label.config(text=output)

frame1 = ttk.Frame(borderwidth=1, relief=SOLID, padding=[5, 5])
frame1.pack(anchor=NW, padx=5, pady=1)

label1 = ttk.Label(frame1)
label1.pack()

z1(label1)



label_all = ttk.Label(textvariable=tasks_var)
label_all.pack(anchor=SW, padx=6, pady=6)


root.mainloop()