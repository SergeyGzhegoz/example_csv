import csv

csv_file = []


# Открыть файл
def file_open(file_name):
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            csv_file.append(row)
        print("Файл открыт. Записей: ", len(csv_file))


# Добавление
def insert(fio, age, tel, otd):
    try:
        mx = max(csv_file, key=lambda x: int(x['ном']))
        csv_file.append({'ном': int(mx['ном']) + 1,
                         'фио': fio,
                         'возраст': age,
                         'телефон': tel,
                         'отдел': otd})
    except Exception as e:
        return f"Ошибка при добавлении новой записи {e}"
    print("Данные добавлены")


# Удаление
def drop_by_arg(val, col_name="фио"):
    global csv_file
    try:
        csv_file = list(filter(lambda x: x[col_name] != val, csv_file))
    except Exception as e:
        return f"Строка со значением {val} поля {col_name} не найдена"
    return f"Строка со значением {val} поля {col_name} удалена!"


# Поиск
def find(val, col_name='фио'):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))


# Средний возраст
def avg_age():
    print("Средний возраст: ", sum([int(row['возраст']) for row in csv_file]) // len(csv_file))


# Сохранить
def save(fine_name):
    with open(fine_name, 'w', encoding='utf-8', newline='') as file:
        columns = ['ном', 'фио', 'возраст', 'телефон', 'отдел']
        writer = csv.DictWriter(file, delimiter=";", fieldnames=columns)
        writer.writeheader()
        writer.writerows(csv_file)
        print('Данные сохранены!')


# Вывод списка записей
def show_rows():
    if len(csv_file) > 0:
        print('{:<5}{:<25}{:<8}{:<12}{:<15}'.format('ном', 'фио', 'возраст', 'телефон', 'отдел'))
        for el in csv_file:
            print('{:<5}{:<25}{:<8}{:<12}{:<15}'.format(el['ном'], el['фио'],
                                                        el['возраст'], el['телефон'], el['отдел']))
