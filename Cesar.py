from collections import deque


alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
shift = int(input('Введите сдвиг - '))
key = input("Введите ключ - ")

for i in key:                           #удаление символов ключа из начального алфавита
    alph = alph.replace(i, '')
alph = key + alph                       #добавление ключа в алфавит
d = deque(alph)                         #сдвиг алфавита
d.rotate(shift)
alph = (''.join(list(d)))

#print(alph)
print("Новый алфавит:", alph)

f = open('text.txt', 'rt', encoding='utf-8')
#message = input("Введите сообщение")
message = f.read().lower()
print('Исходное сообщение:', '\n', message, '\n')
enc_message = ""
dec_message = ""

for sign in message:                            #шифровка введенного сообщения
    index = alph.find(sign)
    newIndex = index + shift
    if newIndex >= len(alph):
        newIndex -= len(alph)
    if sign in alph:
        enc_message = enc_message + alph[newIndex]
    else:
        enc_message = enc_message + sign

print("Зашиврованное сообщение:", '\n', enc_message, '\n')

orig_big = {} #биграм в тексте
enc_big = {}  #биграм в зашифрованном тексте

#частота втречи биграм
for i in range(len(message)):
    if message[i] in alph and message[i + 1] in alph:
        di = message[i] + message[i+1]
        if di in orig_big.keys():
            orig_big[di] += 1
        else:
            orig_big.setdefault(di, 1)


def sort(dic):
    dic = {k: dic[k] for k in sorted(dic, key=dic.get, reverse=True)}
    return dic

orig_big = sort(orig_big)
#print(orig_big)

for i in range(len(enc_message)):
    if enc_message[i] in alph and enc_message[i + 1] in alph:
        di = enc_message[i] + enc_message[i + 1]
        if di in enc_big.keys():
            enc_big[di] += 1
        else:
            enc_big.setdefault(di, 1)

enc_big = sort(enc_big)
#print(enc_big)

mg = []
ch = 0

#формируем словарь соспоставлений расш/заш бигр
for k in orig_big.keys():
    mg.append(k)

for k in enc_big.keys():
    enc_big[k] = mg[ch]
    ch += 1

#print(enc_big)
mono_lang = {"а": 40487008, "б": 8051767, "в": 22930719, "г": 8564640, "д": 15052118,
            "е": 42691213, "ё": 184928, "ж": 4746916, "з": 8329904, "и": 37153142,
            "й": 6106262, "к": 17653469, "л": 22230174, "м": 16203060, "н": 33838881,
            "о": 55414481, "п": 14201572, "р": 23916825, "с": 27627040, "т": 31620970,
            "у": 13245712, "ф": 1335747, "х": 4904176, "ц": 2438807, "ч": 7300193,
            "ш": 3678738, "щ": 1822476, "ъ": 185452, "ы": 9595941,
            "ь": 8784613, "э": 1610107, "ю": 3220715, "я": 10139085}

mono_lang = sort(mono_lang)
#print("Частотность букв в русском языке:", monoLang)

monograms = {"а": 0, "б": 0, "в": 0, "г": 0, "д": 0,
           "е": 0, "ё": 0, "ж": 0, "з": 0, "и": 0,
           "й": 0, "к": 0, "л": 0, "м": 0, "н": 0,
           "о": 0, "п": 0, "р": 0, "с": 0, "т": 0,
           "у": 0, "ф": 0, "х": 0, "ц": 0, "ч": 0,
           "ш": 0, "щ": 0, "ъ": 0, "ы": 0, "ь": 0,
           "э": 0, "ю": 0, "я": 0}

for s in range(len(alph)):
    count = 0
    for l in range(len(enc_message)):
        if enc_message[l] == alph[s]:
            count += 1
    monograms[alph[s]] = count              #print("Встречено букв", alphabet[s], ":", count)

monograms = sort(monograms)              #print("Частотность букв в зашифрованном сообщении:", '\n', monograms)
mg1 = []
ch1 = 0

#словарь сопоставлений монограм
for k in mono_lang.keys():
    mg1.append(k)

for k in monograms.keys():
    monograms[k] = mg1[ch1]
    ch1 += 1

#print(monograms)

#фомируем словарь расшифровки
enc_dic = {}
for k in enc_big.keys():
    if not (k[0] in enc_dic.keys()) and not (k[1] in enc_dic.keys()):
        if not (enc_big[k][0] in enc_dic.values()) and not (enc_big[k][1] in enc_dic.values()):
            enc_dic.setdefault(k[0], enc_big[k][0])
            enc_dic.setdefault(k[1], enc_big[k][1])

for k in monograms.keys():
    if not(k in enc_dic.keys()):
        if not (monograms[k] in enc_dic.values()):
            enc_dic.setdefault(k, monograms[k])

#print(enc_dic)
#недостающие ключи и значения (добираем в словарь)
lost_k = []
lost_values = []
for sign in alph:
    if not(sign in enc_dic.keys()):
        lost_k.append(sign)

for sign in alph:
    if not(sign in enc_dic.values()):
        lost_values.append(sign)

#print(lost_k)
#print(lost_v)

for i in range(len(lost_k)):
    enc_dic.setdefault(lost_k[i], lost_values[i])

#print(enc_dic)
#дишифровка
for sign in enc_message:
    if sign in alph:
        dec_message += enc_dic[sign]
    else:
        dec_message += sign
print('Дишифрованное сообщение', '\n', dec_message)