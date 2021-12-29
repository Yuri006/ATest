#!/usr/bin/env python

import cgi
import cgitb

h1 = '''{
        text-align: center;
        font-family: BreezeSans;
        color: #785aa6;
        font-size: 200%
        }'''


def saving(p):
    old = get()
    with open("result.txt", 'w', encoding='utf-8') as f:
        for i in range(len(old)):
            f.write(str(old[i] + int(i == p)) + '\n')
    f.close()


def create():
    f = open("result.txt", 'w', encoding='utf-8')
    for i in range(6):
        f.write(str(0) + '\n')
    f.close()


def get():
    f = open("result.txt", 'r', encoding='utf-8')
    r = f.read().split()
    f.close()
    r = [int(i) for i in r]
    return r


def processing(form):
    result = ['флегматик', 'холерик', 'меланхолик', 'сангвиник', 'идеальный']
    fake = {
        'y': {6, 24, 36},
        'n': {12, 18, 30, 42, 48, 54}
    }
    ex = {
        'y': {1, 3, 8, 10, 13, 17, 22, 25, 27, 39, 44, 46, 49, 53},
        'n': {5, 15, 20, 29, 32, 34, 37, 41, 51}
    }
    intr = {
        'y': {2, 4, 7, 9, 11, 14, 16, 19, 21, 23, 26, 28, 31, 33, 35, 38, 40, 43, 45, 47, 50, 52, 55, 57}
    }
    fake_r = 6 + len(fake['y'].intersection(set(form))) - len(fake['n'].intersection(set(form)))
    ex_r = 9 - len(ex['n'].intersection(set(form))) + len(ex['y'].intersection(set(form)))
    intr_r = len(intr['y'].intersection(set(form)))
    if fake_r <= 4:
        saving(0)
        return f"""<html>
<head>
    <meta charset="UTF-8">
</head>
<style>
    h1{h1}
</style>
<body>
    <h1>Вы ВРУУУУН, прошедших тест, таких как вы {get()[0]}</h1>
</body>
</html>"""
    else:
        if ex_r < 12 and intr_r < 12:
            r = 0
        elif ex_r < 12 and intr_r > 12:
            r = 2
        elif ex_r > 12 and intr_r < 12:
            r = 3
        elif ex_r > 12 and intr_r > 12:
            r = 1
        else:
            r = 4
        saving(r + 1)
        return f"""<html>
<head>
    <meta charset="UTF-8">
</head>
<style>
    h1{h1}
</style>
<body>
    <h1>Вы {result[r]}, прошедших тест, таких как вы {get()[r + 1]}</h1>
</body>
</html>"""


cgitb.enable()

print("Content-type: text/html")

print("")

print(processing([int(i) for i in cgi.FieldStorage().keys()]))
