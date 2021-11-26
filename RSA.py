import math
import random

def RSA(p, q):
    n = p * q
    w = (p - 1) * (q - 1)
    e = 0
    for i in range(2, w):
        if math.gcd(i, w) == 1:
            e = i
            break
    a = 0
    for i in range(w):
        x = 1+(i*w)
        if x % e == 0:
            a = int(x / e)
            break
    return [e, n], [a, n]

def Miller(d, n):
    a = 2 + random.randint(1, n - 4)
    x = pw(a, d, n)
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False

def Encryption(message, key):
    enc = []
    for m in message:
        enc.append(pow(ord(m), key[0]) % key[1])
    return enc

def Decryption(message, key):
    dec = ''
    for m in message:
        dec += chr(pow(m, key[0]) % key[1])
    return dec

def basic():
    while True:
        num = random.randint(200, 600)
        if test_basic(num, 6) is True: return num

def test_basic(n, k):
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    a = n - 1
    while (a % 2 == 0):
        a //= 2

    for i in range(6):
        if (Miller(a, n) == False):
            return False
    return True

def pw(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

pb_key, pr_key = RSA(basic(), basic())
message = "RSA and Miller"

enc = Encryption(message, pb_key)
print('Public key:', pb_key)
print('Private key:', pr_key)
print("Encrypted: ", enc)

dec = Decryption(enc, pr_key)
print('Decrypted:', dec)