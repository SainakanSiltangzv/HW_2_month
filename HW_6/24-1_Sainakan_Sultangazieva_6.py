#ДЗУрок6 Дэдлайн 25.11.2022 23 59
#ДЗ**: У вас есть файл MOCK_DATA.txt, в котором 1000 строк с данными
# (Имя и Фамилия, емайл, название файла с расширением и код цвета)
#1. Написать программу, где отображается меню с опциями:
# 1 - Считать имена и фамилии, 2 - Считать все емайлы, 3 - Считать названия файлов, 4 - Считать цвета, 5 - Выход
#2. При выборе опции меню необходимо считать соответствующую информацию из файла с данными
# при помощи регулярных выражений и сохранить считанные данные в новый файл.
#3. Если пользователь выбирает пункт в меню 1: считываются все имена и фамилии (1000 строк)
# и сохраняются в файл под названием names.txt.
# Если пользователь выбирает пункт в меню 2: считываются все емайлы (1000 строк)
# и сохраняются в файл под названием emails.txt и тд.
#4. До тех пор пока пользователь не выбрал пункт 5 программа работает и предлагает опции меню.
#5. При повторном выборе какого-то из пунктов меню, существующий файл с данными,
# например names.txt - полностью перезаписывается.
import re

with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
    content = file.read()

    name_list = re.findall(r"\b[A-Z][a-zA-Z\'\-\. ]+[\s]+[a-zA-Z\'\-\. ]+\b", content)
    email_list = re.findall(r'[a-z0-9]+@\S{1,}', content)
    file_list = re.findall(r'[A-Za-z]+\.(?!com|net|org|edu|gov|mil|info|int)[a-z3]{3,5}', content)
    colour_list = re.findall(r'#[a-f0-9]{6}', content)
while True:
    user = int(input('Выберите данные,которые хотите переписать\n'
                     '1 - Считать имена и фамилии, 2 - Считать все емайлы, 3 - Считать названия файлов, 4 - Считать цвета, 5 - Выход '))
    if user == 1:
        with open('name_list.txt', 'w') as name_file:
            name_file.write(str(name_list))
            name_file.close()
    elif user == 2:
        with open('email_list.txt', 'w') as email_file:
            email_file.write(str(email_list))
            email_file.close()
    elif user == 3:
        with open('type_file.txt', 'w') as type_file:
            type_file.write(str(file_list))
            type_file.close()
    elif user == 4:
        with open('colour_file.txt', 'w') as colour_file:
            colour_file.write(str(colour_list))
            colour_file.close()
    elif user == 5:
        break
    else:
        print('Вы не правильно ввели запрос,повторите попытку.')
        continue

#проверка количества:
print(len(name_list),'1(Ф.И.)')
print(len(email_list),'2(почта)')
print(len(file_list),'3(файлы)')
print(len(colour_list),'4(цвета)')

