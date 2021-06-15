'''
task1
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

file_1 = open('task1.txt', 'w')
line = input('Введите текст \n')
while line:
    file_1.writelines(line + '\n')
    line = input('Введите текст \n')
    if not line:
        break

file_1.close()
file_1 = open('task1.txt', 'r')
content = file_1.readlines()
print(f'You entered: {content}')
file_1.close()
