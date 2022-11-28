from emp_csv import file_open, insert, show_rows, save

FILENAME = "data.csv"

MENU = {
    '1': 'Открыть файл',
    '2': 'Добавить',
    '3': 'Удалить',
    '4': 'Найти по значению',
    '5': 'Вывести средний возраст',
    '6': 'Сохранить в файл',
    '7': 'Вывести записи',
    '0': '<- Меню',
    'exit': 'Выход'
}

for k, v in MENU.items():
    print(k, '-', v)

while True:
    action = input('>_')
    if action == '1':
        file_open(FILENAME)
    elif action == '2':
        insert(input('ФИО: '), input('Возраст: '), input('Телефон: '), input('Отдел: '))
    elif action == '6':
        save(FILENAME)
    elif action == '7':
        show_rows()
    elif action == 'exit':
        break
