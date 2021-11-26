from itertools import islice
from collections import Counter
from Cesar_calc import Calc
import re


def Text(file_name):
    with open(file_name, encoding='utf-8') as file:
        res = ''
        for line in file:
            res += line

        return res

def Cesar(mess):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ \n'
    f = {char: 0 for char in alphabet }
    with open('text1.txt', encoding='utf-8') as file:
        for line in file:
            for char in line:
                char = char.upper()
                if char != ' ':
                    char = char.upper()
                    if char in f.keys():
                        f[char] += 1
                    else:
                        f[char] = 1

    res = []
    lett = [' ', 'О', 'А', 'Е', 'И', 'Е', 'Н', 'Л',
                           'Р', 'С', 'В', 'К', 'М', 'Д', 'У', 'П',
                           'Б', 'Г', 'T', 'Ы', 'Ч', 'Ь', 'З', 'Я', 'Й',
                           'Х', 'Ж', 'Ш', 'Ю', 'Ф', 'Э', 'Щ',
                           'Ё', 'Ц', 'Ъ', '\n']

    d = dict(zip(f, lett))
    for i in mess:
        if i in lett:
            res.append(d.get(i))
            res.append(i)

    return ''.join(res)


def bigram(mess, text):
    t = re.findall("\w{2}", text)
    b = Counter(islice(t, 1, None))

    t = re.findall("\w{2}", mess)
    s_b = Counter(islice(t, 1, None))
    for i, y in zip(s_b.most_common(), b.most_common()):
        mess = mess.replace(i[0], y[0])
    return mess


def main():
    text = Text('text.txt')
    text = text.upper()
    print(text)
    print('\n\n\n\n')
    res = Calc(text, 6)
    print('\n\n\n\n')
    print(res)
    c = Cesar(res)
    print('\n\n\n\n')
    print(c)
    print('\n\n\n\n')
    return bigram(res, text)


if __name__ == '__main__':
    print(main())