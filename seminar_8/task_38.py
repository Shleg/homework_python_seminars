# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def show_contacts(filename):
    print('\nСодержание справочника:')
    with open(filename, 'r') as file:
        for index, line in enumerate(file.readlines(), 1):
            print(f'{index}: {line.strip()}')


def find_contact(value, filename):
    flag = False
    with open(filename, 'r') as file:
        for index, line in enumerate(file.readlines(), 1):
            if value.lower() in line.lower():
                flag = True
                print(f'{index}: {line.strip()}')

    if not flag:
        print(f'Контакта с фамилией {value} не найдено')


def add_contact(value, filename):
    with open(filename, 'a') as file:
        file.write('\n' + value)


def change_contact(value, filename):
    flag = False
    with open(filename, 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if value.lower() in line.lower():
                new_value = input('Введите новые имя, фамилию и телефон через пробел: ')
                lines[index] = new_value + '\n'
                flag = True

    if flag:
        with open(filename, 'w') as file:
            file.writelines(lines)
            print('Контакт успешно изменен.')
    else:
        print(f'Контакта с фамилией "{value}" не найдено')




def delete_contact(value, filename):
    flag = False
    with open(filename, 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if value.lower() in line.lower():
                del lines[index]
                flag = True

    if flag:
        with open(filename, 'w') as file:
            file.writelines(lines)
            print('Контакт успешно удален.')
    else:
        print(f'Контакта с фамилией "{value}" не найдено')


def main():
    filename = 'phones.txt'
    while True:
        select = int(input('\nДоступные команды: '
                           '\n1 - показать справочник'
                           '\n2 - найти контакт'
                           '\n3 - добавить контакт'
                           '\n4 - изменить контакт'
                           '\n5 - удалить контакт'
                           '\n6 - для выхода введите любой символ, кроме [1, 2, 3]'
                           '\nВыберите действие: '))

        if select == 1:
            show_contacts(filename)
        elif select == 2:
            request = input('Введите имя или фамилию: ')
            find_contact(request, filename)
        elif select == 3:
            request = input('Введите имя, фамилию и телефон через пробел: ')
            add_contact(request, filename)
        elif select == 4:
            show_contacts(filename)
            contact = input('Какой контакт Вы хотите изменить (введите фамилию, имя или телефон ): ')
            change_contact(contact, filename)
        elif select == 5:
            show_contacts(filename)
            contact = input('Какой контакт Вы хотите удалить (введите фамилию, имя или телефон ): ')
            delete_contact(contact, filename)
        else:
            break


if __name__ == '__main__':
    main()
