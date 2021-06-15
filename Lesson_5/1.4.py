'''
task4
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('task4.txt', 'r', encoding='utf-8') as basic_file:
    with open('task4_tr.txt', 'w', encoding='utf-8') as trans_file:
        for line in basic_file:
            en, *num = line.split()
            ru = trans[en]
            trans_file.write(' '.join([ru] + num) + '\n')

# from googletrans import Translator as gt
#
# trl = gt()
# with open('task4.txt', 'r', encoding="utf-8") as basic_file:
#     content = [stroke.strip().split() for stroke in basic_file]
# for el in content:
#     el.insert(0, trl.translate(el.pop(0)))
# content = [' '.join(el) for el in content]
# with open('task4_tr.txt', 'w', encoding="utf-8") as trans_file:
#     for el in content:
#         trans_file.writelines(f'{el}\n')
