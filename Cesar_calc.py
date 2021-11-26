def Calc(mess, step):
    A = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    res = ''
    mess = mess.upper()
    for i in mess:
        char = A.find(i)
        new_char = char + step
        if i in A:
            res += A[new_char]
        else:
            res += i

    return res

if '__main__' == __name__:
    s = int(input('Step: '))
    mes = input("Message: ").upper()
    print(Calc(mes, s))