from input_data import data_directory as contact

def loger_txt(contact):
    with open('directory.txt', 'a', encoding = 'utf-8') as file:
        file.write(str(contact))
    print('Контакт успешно внесён в формате .txt')

def loger_csv(contact):
    with open('directory_1.csv', 'a', encoding = 'utf-8') as file:
        file.write(str(contact))
    print('Контакт успешно внесён в формате .csv')
    print('---------------------------------------------')
