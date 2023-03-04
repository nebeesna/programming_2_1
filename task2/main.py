# Завдання 2: (3 бали)
# Створити тип транспортний маршрут
# (початкова станція, кінцева станція, к-сть зупинок, протяжність маршруту в км).
# Дані про маршрути задаються у файлі.
# Створити список маршрутів.
# Посортувати його за протяжністю.
# Вивести к-сть маршрутів, для яких середня довжина між зупинками менша за X.
# Створити список маршрутів, які починаються в станції Х.
# Вивести маршрути з максимальною к-стю зупинок.
class TransportRoute:
    def __init__(self, start_st='', end_st='', count_of_st=0, route_len=0.0):
        self._start_st = start_st
        self._end_st = end_st
        self._count_of_st = count_of_st
        self._route_len = route_len

    def __gt__(self, other):
        return self._route_len > other._route_len

    def __lt__(self, other):
        return self._route_len < other._route_len

    @property
    def get_start_st(self):
        return self._start_st

    @property
    def get_end_st(self):
        return self._end_st

    @property
    def get_stops(self):
        return self._count_of_st

    @property
    def get_len(self):
        return self._route_len

    def input(self, line):
        self._start_st, self._end_st, self._count_of_st, self._route_len = line.split()
        self._count_of_st = int(self._count_of_st)
        self._route_len = float(self._route_len)

    def __str__(self):
        return f"Start stop: {self._start_st}\nLast stop: {self._end_st}\nCount of stops: {self._count_of_st}\n" \
               f"Length of route: {self._route_len} km \n"


def count_stops(rt, x):
    count = 0
    for r in rt:
        if (r.get_len / r.get_stops) < x:
            count += 1
        else:
            continue
    print(f"K-сть маршрутів, для яких середня довжина між зупинками менша за {x}: {count}")


def starts_in_x(rt, x):
    new_rt = []
    for r in rt:
        if r.get_start_st == x:
            new_rt.append(r)
        else:
            continue
    return new_rt


def max_count_of_stops(rt):
    max_st = 0
    for r in rt:
        if r.get_stops > max_st:
            max_st = r.get_stops
    for r in rt:
        if r.get_stops == max_st:
            print(r)


routes = []
f = open("data_of_routes.txt")
i = 0
for line in f:
    routes.append(TransportRoute())
    routes[i].input(line)
    i += 1

print("Посортувати його(список) за протяжністю:\n")
routes.sort()
for i in routes:
    print(i)

print("Введіть Х для розрахунку к-сті маршрутів у яких середня довжина менша ніж Х:")
x = float(input("x = "))
count_stops(routes, x)

x = input("\nВведіть назву потрібної початкої станції: ")
new_routes = starts_in_x(routes, x)
print(f"Станції які починаються з {x}:\n")
for i in new_routes:
    print(i)

print("Маршрути з максимальною к-стю зупинок:")
max_count_of_stops(routes)


