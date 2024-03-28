import json


# на Отлично в одного человека надо сделать консольное приложение Телефонный справочник с внешним хранилищем информации,
# и чтоб был реализован основной функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных.
def rules():
    print('\n Команды работы со справочником \n'
          '1 - просмотр всех конткактов \n'
          '2 - создание новых конткактов \n'
          '3 - импорт \n'
          '4 - поиск \n'
          '5 - редактирование данных \n'
          '5 - остановка при уведомлениях \n'
          '7 - завершение работы программы')


def rules_s():
    print('\n Список команд \n'
          '1 - добавить или изменить имя ползователя \n'
          '2 - добавить или изменить номера телефонов \n'
          '3 - добавить или изменить дату рождения \n'
          '4 - добавить или изменить описание \n'
          '5 - вывести данные в терминале\n'
          '6 - сохранить данные \n'
          '7 - вернутся назад \n')


def err():
    print("\n Такой команды не существует")
    stop()


def stop():
    if setting:
        input('Enter что-бы продолжить\n-> ')


def confirmation():
    a = input('\nПродолжить?\n1 - Продолжить\n2 - Отмена\n-> ')
    if a == '1':
        return True
    else:
        return False


def reset():
    return {'/non_data': {'phone_numb': [], 'b_date': 'Нет данных', 'description': 'Нет данных'}}, '/non_data'


def load_data():
    try:
        with open("phone_db.json", "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_data(data):
    with open("phone_db.json", "w", encoding="UTF-8") as file:
        json.dump(data, file, ensure_ascii=False)


def conti_save(char, name):
    old_data = load_data()
    old_data[name] = char[name].copy()
    save_data(old_data)
    print('\nДанные были успешно сохранены')
    stop()


def new_data():
    char = {'/non_data': {'phone_numb': [], 'b_date': 'Нет данных', 'description': 'Нет данных'}}
    stock = {'/non_data': {'phone_numb': [], 'b_date': 'Нет данных', 'description': 'Нет данных'}}
    name = '/non_data'
    while True:
        rules_s()
        cmd = input('-> ')
        if cmd == '1':
            char[name := input('\nВведите имя\n-> ')] = char.pop(name)
        elif cmd == '2':
            numbers = input('\nВведите номера через прробел\n!Внимание! внутри номера не должно быть пробелов\n'
                            '+7 999 999 99 99 X \n+7-999-999-99-99 V\n-> ').split()
            char[name]['phone_numb'] = numbers
        elif cmd == '3':
            char[name]['b_date'] = input('\nВведите дату рождения\n-> ')
        elif cmd == '4':
            char[name]['description'] = input('\nВведите описание контакта\n-> ')
        elif cmd == '5':
            print()
            print(f'Имя: {name}\nТелефон: {char[name]['phone_numb']}\nДата рождения: {char[name]['b_date']}\n'
                  f'Описание: {char[name]['description']}')
            stop()
        elif cmd == '6':
            if name == '/non_data':
                print('\nВы не ввели имя')
                stop()
            elif len(char[name]['phone_numb']) == 0:
                print('\nВы не ввели номер телефона')
                if confirmation():
                    conti_save(char, name)
                    char, name = reset()
            elif stock == char:
                print('\nВы ничего не ввели')
                stop()
            else:
                conti_save(char, name)
                char, name = reset()
        elif cmd == '7':
            if stock == char:
                return
            else:
                print('\nНе сохраненые данные будут утерены')
                if confirmation():
                    return
        else:
            err()


# def edit_contact(cmd, name, char={'/non_data': {'phone_numb': [], 'b_date': 'Нет данных', 'description': 'Нет данных'}},
#                  stock={'/non_data': {'phone_numb': [], 'b_date': 'Нет данных', 'description': 'Нет данных'}}):
#     if cmd == '1':
#         char[name := input('\nВведите имя\n-> ')] = char.pop(name)
#     elif cmd == '2':
#         numbers = input('\nВведите номера через прробел\n!Внимание! внутри номера не должно быть пробелов\n'
#                         '+7 999 999 99 99 X \n+7-999-999-99-99 V\n-> ').split()
#         char[name]['phone_numb'] = numbers
#     elif cmd == '3':
#         char[name]['b_date'] = input('\nВведите дату рождения\n-> ')
#     elif cmd == '4':
#         char[name]['description'] = input('\nВведите описание контакта\n-> ')
#     elif cmd == '5':
#         print()
#         print(f'Имя: {name}\nТелефон: {char[name]['phone_numb']}\nДата рождения: {char[name]['b_date']}\n'
#               f'Описание: {char[name]['description']}')
#         stop()
#     elif cmd == '6':
#         if name == '/non_data':
#             print('\nВы не ввели имя')
#             stop()
#         elif len(char[name]['phone_numb']) == 0:
#             print('\nВы не ввели номер телефона')
#             if confirmation():
#                 conti_save(char, name)
#                 char, name = reset()
#         elif stock == char:
#             print('\nВы ничего не ввели')
#             stop()
#         else:
#             conti_save(char, name)
#             char, name = reset()
#     elif cmd == '7':
#         if stock == char:
#             return
#         else:
#             print('\nНе сохраненые данные будут утерены')
#             if confirmation():
#                 return
#     else:
#         err()


def view_all():
    result = load_data()
    if not result:
        print('\nТелефонный справочник пуст\n')
    else:
        for name, data in result.items():
            print()
            print('-' * 10)
            print(f'Имя: {name}')
            print(f'Тефон: {data['phone_numb']}')
            print(f'Дата рожденя: {data['b_date']}')
            print(f'Описани: {data['description']}')
            print('-' * 10)
    stop()


def edit_save(con):
    try:
        save_data(con)
    except Exception:
        input("Еще не было изменений")


def edit_data():
    while True:
        cmd = input('\nСписок команд\n1 - изменить контакт\n2 - удалить данные\n3 - вернутся назад\n-> ')
        if cmd == '1':
            name = input("\nВведите имя контакта\n-> ")

        elif cmd == '2':
            n = input("\nВведите имя контакта или /all что-бы удалить все\n-> ")
            if n == '/all' and confirmation():
                edit_save({})
            else:
                con = load_data()
                if n not in con:
                    print("\nТакого контакта еще нет")
                    stop()
                elif confirmation():
                    del con[n]
                    edit_save(con)
                    print('Удалено')
                    stop()
        elif cmd == '3':
            return
        else:
            err()


setting = True


def main():
    global setting
    while True:
        rules()
        n = input('-> ')
        if n == '1':
            view_all()
        elif n == '2':
            new_data()
        elif n == '3':
            print('Эта функция еще не реалезована')# я так и не понял что подразумевается под импортом
        elif n == '4':
            pass
        elif n == '5':
            edit_data()
        elif n == '6':
            setting = not setting
            print('Настройки изменены')
        elif n == '7':
            break
        else:
            err()
    print('\n Работа программы прекращена')


main()
