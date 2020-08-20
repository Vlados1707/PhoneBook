from tkinter import *
import os

Birthday_sp = dict()


def clear():
    input_tel.delete(0, END)
    input_last_name.delete(0, END)
    input_first_name.delete(0, END)
    input_patronymic.delete(0, END)
    input_address.delete(0, END)


def add():
    tel = input_tel.get()
    if tel in Birthday_sp:
        label_info.config(text="Такая дата уже существует")
    else:
        value = list()
        value.append(input_last_name.get())
        value.append(input_first_name.get())
        value.append(input_patronymic.get())
        value.append(input_address.get())
        Birthday_sp[tel] = value

        list_tel.insert(END, tel)


def select_list_tel(event):
    w = event.widget
    i = int(w.curselection()[0])
    tel = w.get(i)

    value = Birthday_sp[tel]
    last_name = value[0]
    first_name = value[1]
    patronymic = value[2]
    address = value[3]

    clear()
    input_tel.insert(0, tel)
    input_last_name.insert(0, last_name)
    input_first_name.insert(0, first_name)
    input_patronymic.insert(0, patronymic)
    input_address.insert(0, address)


window = Tk()
window.title("Birthday")
window.geometry("500x250")

# Объявление элементов окна
label_tel = Label(text="Дата дня рождения")
input_tel = Entry()

label_last_name = Label(text="Фамилия")
input_last_name = Entry()

label_first_name = Label(text="Имя")
input_first_name = Entry()

label_patronymic = Label(text="Отчество")
input_patronymic = Entry()

label_address = Label(text="Адрес")
input_address = Entry()

button_add = Button(text="Добавить", command=add)
button_clear = Button(text="Очистить", command=clear)

label_list_tel = Label(text="Список дат")
list_tel = Listbox()

label_info = Label(text="Внесите данные именинников")

# Позиционирование
label_tel.grid(row=0, column=0, padx=10, pady=5, sticky="w")
input_tel.grid(row=0, column=1)

label_last_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")
input_last_name.grid(row=1, column=1, padx=10)

label_first_name.grid(row=2, column=0, padx=10, pady=5, sticky="w")
input_first_name.grid(row=2, column=1)

label_patronymic.grid(row=3, column=0, padx=10, pady=5, sticky="w")
input_patronymic.grid(row=3, column=1, padx=10)

label_address.grid(row=4, column=0, padx=10, pady=5, sticky="w")
input_address.grid(row=4, column=1, pady=15)

button_add.grid(row=1, column=2, padx=10)
button_clear.grid(row=3, column=2, padx=10)

label_list_tel.grid(row=0, column=3)
list_tel.grid(row=1, column=3, rowspan=4, pady=15)

label_info.grid(row=5, column=0, columnspan=4, sticky="w")

list_tel.bind('<<ListboxSelect>>', select_list_tel)

if os.path.exists("Birthday.csv"):
    with open("Birthday.csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split(";")
            tel = elements[0]
            last_name = elements[1]
            first_name = elements[2]
            patronymic = elements[3]
            address = elements[4]
            value = list()
            value.append(last_name)
            value.append(first_name)
            value.append(patronymic)
            value.append(address)
            Birthday_sp[tel] = value
            list_tel.insert(END, tel)

window.mainloop()