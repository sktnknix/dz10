# -*- coding: utf-8 -*-

from datetime import datetime

class TimeScore(object):
    def __enter__(self):
        self.progstart = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Скрипт запустился в ' + str(self.progstart))
        print('Скрипт закончил работу в ' + str(datetime.now()))
        print("Время выполнения: " + str(datetime.now() - self.progstart))

with TimeScore() as ts:
    zero = [" *** ",
            " * * ",
            "*   *",
            "*   *",
            "*   *",
            " * * ",
            " *** "]
    one = ["  **",
           " * *",
           "   *",
           "   *",
           "   *",
           "   *",
           "   *"]
    two = [" *** ",
           "*   *",
           "*   *",
           "   * ",
           "  *  ",
           " *   ",
           "*****"]
    three = [" *** ",
             "*   *",
             "    *",
             " *** ",
             "    *",
             "*   *",
             " *** "]
    four = ["   *",
            "  **",
            " * *",
            "*  *",
            "******",
            "   *",
            "   *"]
    five = ["*****",
            "*    ",
            "*    ",
            " *** ",
            "    *",
            "    *",
            "****"]
    six = [" **  ",
           "*    ",
           "*    ",
           "**** ",
           "*   *",
           "*   *",
           " *** "]
    seven = ["*****",
             "    *",
             "   * ",
             "  *  ",
             " *   ",
             "*    ",
             "*    "]
    eight = [" *** ",
             "*   *",
             "*   *",
             " *** ",
             "*   *",
             "*   *",
             " *** "]
    nine = [" ****",
            "*   *",
            "*   *",
            " ****",
            "    *",
            "    *",
            "   **"]
    _digital = {0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine}

    ent = input('Введите несколько цифр: ')

    d = []
    for i in ent:
        d.append(_digital[int(i)])

    _res = d

    sum = []

    for k in _res:
        sum += k

    l = 0

    while l < 7:
        print('\t'.join(sum[l::7]))
        l += 1