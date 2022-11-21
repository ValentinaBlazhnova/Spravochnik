from input_data import data_directory
from log import  loger_txt, loger_csv
from view_data import searching_contact

def menu():
    print('Введите "0", если хотите добавить контакт ')
    print('Введите "1", если хотите просмотреть контакт')
    flag = int(input())
    if flag == 0:
        add_contact = data_directory()
        loger_txt(add_contact)
        loger_csv(add_contact)
        print('Введите "0", если хотите добавить контакт ')
        print('Введите "1", если хотите просмотреть контакт')
    elif flag == 1:
        print(searching_contact())
    else:
        print("Введите 0 или 1")


