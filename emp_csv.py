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


# Вывод списка записей
def show_rows():
    if len(csv_file) > 0:
        print('{:<5}{:<25}{:<8}{:<12}{:<15}'.format('ном', 'фио', 'возраст', 'телефон', 'отдел'))
        for el in csv_file:
            print('{:<5}{:<25}{:<8}{:<12}{:<15}'.format(el['ном'], el['фио'],
                                                        el['возраст'], el['телефон'], el['отдел']))
