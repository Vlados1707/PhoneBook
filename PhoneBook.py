# *** PhoneBook ***
#
# tel - номер телефона, строка
# first_name - имя, строка
# last_name - фамилия, строка
# patronymic - отчество, строка
# address - адрес, строка
# {tel: [last_name, first_name, patronymic, address]}


from phonebook_lib import *

phone_book = dict()

welcome()

menu()
choice = int(input("Введите режим работы: "))

if choice == 1:
    print((phone_book))
elif choice == 2:
    tel = input("Введите номер телефона: ")
    value = input_data()
    phone_book[tel] = value
elif choice == 3:  # TODO Редактирование записи
    print()
elif choice == 4:  # TODO Удаление записи
    print()
elif choice == 0:  # TODO Выход
    print()
else:
    print("Неправильный режим")
print(phone_book)
