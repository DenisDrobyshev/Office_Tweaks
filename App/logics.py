import os
from pdf2docx import parse
from docx2pdf import convert
from PIL import Image


def PDF_to_Docx(catalog):
    print('Список файлов с расширением .pdf:')
    list_files = os.listdir(catalog)
    lst = []
    count = 0
    for file in list_files:
        if '.pdf' in file:
            count += 1
            print(f'{count}. {file}')
            lst.append(file)
    answer = int(input('Введите номер файла для преобразования (если хотите преобразовать все файлы из данного '
                       'каталога, введите 0): '))
    try:
        if answer == 0:
            for file in lst:
                pdf_file = fr'{catalog}/{file}'
                docx_file = fr'{catalog}/{file}'
                docx_file = docx_file.replace('.pdf', '.docx')
                parse(pdf_file, docx_file)
        else:
            pdf_file = fr'{catalog}/{lst[answer - 1]}'
            docx_file = fr'{catalog}/{lst[answer - 1]}'
            docx_file = docx_file.replace('.pdf', '.docx')
            parse(pdf_file, docx_file)
    except IndexError:
        print('Ошибка! Вы ввели некорректные данные')


def Docx_to_PDF(catalog):
    print('Список файлов с расширением .Docx:')
    list_files = os.listdir(catalog)
    lst = []
    count = 0
    for file in list_files:
        if '.docx' in file:
            count += 1
            print(f'{count}. {file}')
            lst.append(file)
    answer = int(input('Введите номер файла для преобразования (если хотите преобразовать все файлы из данного '
                       'каталога введите 0): '))
    try:
        if answer == 0:
            for file in lst:
                pdf_file = fr'{catalog}/{file}'
                docx_file = fr'{catalog}/{file}'
                pdf_file = pdf_file.replace('.docx', '.pdf')
                convert(docx_file, pdf_file)
        else:
            pdf_file = fr'{catalog}/{lst[answer - 1]}'
            docx_file = fr'{catalog}/{lst[answer - 1]}'
            pdf_file = pdf_file.replace('.docx', '.pdf')
            convert(docx_file, pdf_file)
    except IndexError:
        print('Ошибка! Вы ввели некорректные данные')


def compress_image(catalog):
    print("Список файлов с расширением ('.jpeg', '.gif', '.png' ,'.jpg'):")
    list_files = os.listdir(catalog)
    lst = []
    count = 0
    for file in lst:
        if ('.jpeg' in file) or ('.gif' in file) or ('.png' in file) or ('.jpg' in file):
            count += 1
            print(f'{count}. {file}')
            lst.append(file)
    answer = int(input('Введите номер файла для преобразования (если хотите преобразовать все файлы из данного '
                       'каталога введите 0): '))
    answer2 = int(input('Введите параметры сжатия (от 0 до 100%): '))
    if answer == 0:
        for file in lst:
            image_path = file
            image_file = Image.open(image_path)
            image_file.save(image_path, quality=answer2)
    else:
        image_path = lst[answer - 1]
        image_file = Image.open(image_path)
        image_file.save(image_path, quality=answer2)


def delete_files(catalog):
    answer = int(input('Выберите действие:\n'
                       '1. Удалить все файлы начинающиеся на определённую подстроку\n'
                       '2. Удалите все файлы заканчивающиеся на определённую подстроку\n'
                       '3. Удалить все файлы содержащие определённую подстроку\n'
                       '4. Удалить все файлы по расширению\n'
                       'Введите номер действия: '))
    answer2 = input('Введите подстроку: ')
    list_of_files = os.listdir(catalog)
    if answer == 1:
        for file in list_of_files:
            if file.startswith(answer2) == True:
                os.remove(fr"{catalog}/{file}")
                print(f'Файл: {file} успешно удалён!')
    if answer == 2:
        for file in list_of_files:
            if (answer2 + '.') in file:
                os.remove(fr"{catalog}/{file}")
                print(f'Файл: {file} успешно удалён!')
    if answer == 3:
        for file in list_of_files:
            if answer2 in file:
                os.remove(fr"{catalog}/{file}")
                print(f'Файл: {file} успешно удалён!')
    if answer == 4:
        for file in list_of_files:
            if ('.' + answer2) in file:
                os.remove(fr"{catalog}/{file}")
                print(f'Файл: {file} успешно удалён!')
