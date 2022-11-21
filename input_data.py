def data_directory():
    data_base = []
    while True:
        data_base.append({'surname': input('Введите фамилию: '), 'name': input('Введите имя: '), 'tel': input('Введите телефон: '), 'comment': input('Введите описание: ')})
        break
    return data_base
    
#print(data_directory())

# Без словаря:
# def data_directory():
#     surname = input('Введите фамилию: ')
#     name = input('Введите имя:')
#     tel = input('Введите телефон: ')
#     comment = input('Введите описание: ')
#     return surname, name, tel, comment
     