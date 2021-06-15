'''
task2
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

file_2 = open('task2.txt', 'r')
content = file_2.read()
print(f'File contents: \n {content}')
file_2.close()

file_2 = open('task2.txt', 'r')
content = file_2.readlines()
for i in range(len(content)):
    print(f'Number of characters in the file {i + 1}-th line is {len(content[i])};')
file_2.close()

file_2 = open('task2.txt', 'r')
content = file_2.readlines()
print(f'Number of lines in the file: {len(content)}')
file_2.close()

file_2 = open('task2.txt', 'r')
content = file_2.read()
content = content.split()
print(f'The number of words in the file: {len(content)}')
file_2.close()
