def summ(n2):
    n3 = int(n2)

    if (int(n3 / 100000) % 10) == 1:
        d = 'сто'
    elif (int(n3 / 100000) % 10) == 2:
        d = 'двести'
    elif (int(n3 / 100000) % 10) == 3:
        d = 'триста'
    elif (int(n3 / 100000) % 10) == 4:
        d = 'четыреста'
    elif (int(n3 / 100000) % 10) == 5:
        d = 'пятьсот'
    elif (int(n3 / 100000) % 10) == 6:
        d = 'шестьсот'
    elif (int(n3 / 100000) % 10) == 7:
        d = 'семьсот'
    elif (int(n3 / 100000) % 10) == 8:
        d = 'восемьсот'
    elif (int(n3 / 100000) % 10) == 9:
        d = 'девятьсот'
    elif (int(n3 / 100000) % 10) == 0:
        d = ''

    if int(n3 / 10000) % 10 == 1:
        if int(n3 / 1000) % 10 == 0:
            e = 'десять'
        elif int(n3 / 1000) % 10 == 1:
            e = 'одиннадцать'
        elif int(n3 / 1000) % 10 == 2:
            e = 'двенадцать'
        elif int(n3 / 1000) % 10 == 3:
            e = 'тринадцать'
        elif int(n3 / 1000) % 10 == 4:
            e = 'четырнадцать'
        elif int(n3 / 1000) % 10 == 5:
            e = 'пятнадцать'
        elif int(n3 / 1000) % 10 == 6:
            e = 'шестнадцать'
        elif int(n3 / 1000) % 10 == 7:
            e = 'семнадцать'
        elif int(n3 / 1000) % 10 == 8:
            e = 'восемнадцать'
        elif int(n3 / 1000) % 10 == 9:
            e = 'девятнадцать'

    elif int(n3 / 10000) % 10 == 2:
        e = 'двадцать'
    elif int(n3 / 10000) % 10 == 3:
        e = 'тридцать'
    elif int(n3 / 10000) % 10 == 4:
        e = 'сорок'
    elif int(n3 / 10000) % 10 == 5:
        e = 'пятьдесят'
    elif int(n3 / 10000) % 10 == 6:
        e = 'шестьдесят'
    elif int(n3 / 10000) % 10 == 7:
        e = 'семьдесят'
    elif int(n3 / 10000) % 10 == 8:
        e = 'восемьдесят'
    elif int(n3 / 10000) % 10 == 9:
        e = 'девяноста'
    elif int(n3 / 10000) % 10 == 0:
        e = ''

    if (int(n3 / 10000) % 10) != 1:
        if (int(n3 / 1000) % 10) == 1:
            f = 'одна тысяча'
        elif (int(n3 / 1000) % 10) == 2:
            f = 'две тысячи'
        elif (int(n3 / 1000) % 10) == 3:
            f = 'три тысячи'
        elif (int(n3 / 1000) % 10) == 4:
            f = 'четыре тысячи'
        elif (int(n3 / 1000) % 10) == 5:
            f = 'пять тысяч'
        elif (int(n3 / 1000) % 10) == 6:
            f = 'шесть тысяч'
        elif (int(n3 / 1000) % 10) == 7:
            f = 'семь тысяч'
        elif (int(n3 / 1000) % 10) == 8:
            f = 'восемь тысяч'
        elif (int(n3 / 1000) % 10) == 9:
            f = 'девять тысяч'
        elif (int(n3 / 1000) % 10) == 0:
            f = ''

    if (int(n3 / 100) % 10) == 1:
        j = 'сто'
    elif (int(n3 / 100) % 10) == 2:
        j = 'двести'
    elif (int(n3 / 100) % 10) == 3:
        j = 'триста'
    elif (int(n3 / 100) % 10) == 4:
        j = 'четыреста'
    elif (int(n3 / 100) % 10) == 5:
        j = 'пятьсот'
    elif (int(n3 / 100) % 10) == 6:
        j = 'шестьсот'
    elif (int(n3 / 100) % 10) == 7:
        j = 'семьсот'
    elif (int(n3 / 100) % 10) == 8:
        j = 'восемьсот'
    elif (int(n3 / 100) % 10) == 9:
        j = 'девятьсот'
    elif (int(n3 / 100) % 10) == 0:
        j = ''

    if int(n3 / 10) % 10 == 1:
        if (n3 % 10) == 0:
            h = 'десять'
        elif (n3 % 10) == 1:
            h = 'одиннадцать'
        elif (n3 % 10) == 2:
            h = 'двенадцать'
        elif (n3 % 10) == 3:
            h = 'тринадцать'
        elif (n3 % 10) == 4:
            h = 'четырнадцать'
        elif (n3 % 10) == 5:
            h = 'пятнадцать'
        elif (n3 % 10) == 6:
            h = 'шестнадцать'
        elif (n3 % 10) == 7:
            h = 'семнадцать'
        elif (n3 % 10) == 8:
            h = 'восемнадцать'
        elif (n3 % 10) == 9:
            h = 'девятнадцать'

    elif int(n3 / 10) % 10 == 2:
        h = 'двадцать'
    elif int(n3 / 10) % 10 == 3:
        h = 'тридцать'
    elif int(n3 / 10) % 10 == 4:
        h = 'сорок'
    elif int(n3 / 10) % 10 == 5:
        h = 'пятьдесят'
    elif int(n3 / 10) % 10 == 6:
        h = 'шестьдесят'
    elif int(n3 / 10) % 10 == 7:
        h = 'семьдесят'
    elif int(n3 / 10) % 10 == 8:
        h = 'восемьдесят'
    elif int(n3 / 10) % 10 == 9:
        h = 'девяноста'
    elif int(n3 / 10) % 10 == 0:
        h = ''

    if (int(n3 / 10) % 10) != 1:
        if (n3 % 10) == 1:
            g = 'один рубль'
        elif (n3 % 10) == 2:
            g = 'два рубля'
        elif (n3 % 10) == 3:
            g = 'три рубля'
        elif (n3 % 10) == 4:
            g = 'четыре рубля'
        elif (n3 % 10) == 5:
            g = 'пять рублей'
        elif (n3 % 10) == 6:
            g = 'шесть рублей'
        elif (n3 % 10) == 7:
            g = 'семь рублей'
        elif (n3 % 10) == 8:
            g = 'восемь рублей'
        elif (n3 % 10) == 9:
            g = 'девять рублей'
        elif (n3 % 10) == 0:
            g = ''

    i = ''
    if int(n3 // 10000) >= 1 == 0:
        i = 'тысяч'

    u = ''
    if int(n3 % 10) == 0:
        u = 'рублей'

    print(f'Сумма: {d} {e} {f} {i} {j} {h} {g} {u}')


def keys(a, value):
    for k, v in a.items():
        if v == value:
            return k


def calculate_taxi_costs(n):
    sort = {}
    c = 0
    km = {}
    for i in range(n):
        while True:
            try:
                n2 = int(input(f'Введите расстояние от работы до дома для {i + 1} сотрудника: '))
                km[i + 1] = n2
                break
            except ValueError:
                print('Введено неверное значение!')
        c += 1

    c1 = 0
    car = {}
    for i in range(n):
        while True:
            try:
                n3 = int(input(f'Введите тариф в рублях для {i + 1} машины: '))
                car[i + 1] = n3
                break
            except ValueError:
                print('Введено неверное значение!')
        c1 += 1

    car1 = sorted(car.values(), reverse=True)
    km1 = sorted(km.values())
    for i in range(n):
        a1 = car1[i]
        b1 = km1[i]

        a = keys(car, a1)
        b = keys(km, b1)

        sort[b] = a

        del car[a]
        del km[b]

    sort1 = sorted(sort.values())

    person = []
    for i in range(n):
        a2 = sort1[i]
        a3 = keys(sort, a2)
        person.append(str(a3))

    summa = 0
    for i in range(n):
        sum = car1[i] * km1[i]
        summa += sum

    print('Порядок рассадки сотрудников:', ' '.join(person))
    print('Сумма:', summa, 'руб.')
    summ(summa)


while True:
    try:
        n = int(input('Введите количество сотрудников: '))
        if 1 <= n <= 1000:
            break
        else:
            print('Введенно неверное значение!')
    except ValueError:
        print('Введено неверное значение!')

calculate_taxi_costs(n)