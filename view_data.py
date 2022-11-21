from input_data import data_directory as contact

def searching_contact():
    phone_book = open("directory.txt", 'r', encoding = 'utf-8')
    phone_book.writelines
    search = input('Введите фамилию для поиска: ')
    for  i in phone_book:
        if search == i[0]:
            print(contact)
            break
        else:
            print('Нет такого контакта')
            break
    phone_book.close