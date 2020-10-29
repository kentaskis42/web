# используется для сортировки
from operator import itemgetter



class Muzikant:
    """Музыкант"""

    def __init__(self, id, fio, zarplata, orkestr_id):
        self.id = id
        self.fio = fio
        self.zarplata = zarplata
        self.orkestr_id = orkestr_id


class Orkestr:
    """Оркестр"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class MuzOrkestrs:
    """
     Для реализации
     связи многие-ко-многим
     """

    def __init__(self, orkestr_id, muzikant_id):
        self.orkestr_id = orkestr_id
        self.muzikant_id = muzikant_id


# Каталоги
orkestrs = [
    Orkestr(1, 'Оркестр1'),
    Orkestr(2, 'Оркестр2'),
    Orkestr(3, 'Оркестр3'),
]
# Файлы
muzikants = [
    Muzikant(1, 'Белов И.И.', 25000, 1),
    Muzikant(2, 'Чернов А.А.', 35000, 2),
    Muzikant(3, 'Петров П.П.', 45000, 3),
    Muzikant(4, 'Иванов И.И.', 35000, 3),
    Muzikant(5, 'Алексеев А.А.', 25000, 1),
]
muz_orkestrs = [
    MuzOrkestrs(1, 1),
    MuzOrkestrs(2, 2),
    MuzOrkestrs(3, 3),
    MuzOrkestrs(3, 4),
    MuzOrkestrs(3, 5),
]


def main():
    """Основная функция"""


# Соединение данных один-ко-многим
one_to_many = [(e.fio, e.zarplata, d.name)
               for d in orkestrs
               for e in muzikants
               if e.orkestr_id == d.id]
# Соединение данных многие-ко-многим
many_to_many_tDir = [(d.name, ed.orkestr_id, ed.muzikant_id)
                     for d in orkestrs
                     for ed in muz_orkestrs
                     if d.id == ed.orkestr_id]
many_to_many = [(e.fio, e.zarplata, orkestr_name)
                for orkestr_name, orkestr_id, muzikant_id in many_to_many_tDir
                for e in muzikants if e.id == muzikant_id]
print('Задание А1')
res_11 = sorted(one_to_many, key=itemgetter(2))
print(res_11)
print('\n Задание А2 ')
res_12_unsorted = []
for d in orkestrs:
    # Список
    d_muzikants = list(filter(lambda i: i[2] == d.name, one_to_many))
# Если не пустой
if len(d_muzikants) > 0:
    # зарплата музыкантов оркестра
    d_zarplata = [zarplata for _, zarplata, _ in d_muzikants]
    d_zarplata_sum = sum(d_zarplata)
    res_12_unsorted.append((d.name, d_zarplata_sum))
    # Сортировка по суммарной зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)
    print('\n Задание А3')
    res_13 = {}
# Перебираем все оркестры
for d in orkestrs:
    if 'Оркестр' in d.name:
        # Список музыкантов оркестров
        d_muzikants = list(filter(lambda i: i[2] == d.name, many_to_many))
        # Только фио музыканта
        d_muzikants_names = [x for x, _, _ in d_muzikants]
        # Добавляем результат в словарь
        # ключ - отдел, значение - список названий
        res_13[d.name] = d_muzikants_names
print(res_13)
if __name__ == '__main__':
    main()


