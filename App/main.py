from App.logics import *


def menu():
    try:
        catalog = os.getcwd()
        choice = int(input(f'\nТекущий каталог: {catalog}\n\n'
                           'Выберите действие:\n\n'
                           '0. Сменить рабочий каталог\n'
                           '1. Преобразовать PDF в Docx\n'
                           '2. Преобразовать Docx в PDF\n'
                           '3. Произвести сжатие изображений\n'
                           '4. Удалить группу файлов\n'
                           '5. Выход\n\n'
                           'Ваш выбор: '))
        if choice == 0:
            answer = input('Укажите корректный путь к рабочему каталогу: ')
            if os.path.exists(answer) == True:
                os.chdir(answer)
            else:
                print('Такого каталога нет')
        if choice == 1:
            PDF_to_Docx(catalog)
        if choice == 2:
            Docx_to_PDF(catalog)
        if choice == 3:
            compress_image(catalog)
        if choice == 4:
            delete_files(catalog)
        if choice == 5:
            print('До свидания!')
            return 0
        return menu()
    except ValueError:
        print('Введите цифру соответствующую команде')


menu()
