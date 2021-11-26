from math import gcd
import random
import hashlib


def SRP(pswd: str) -> int:
    n = 1
    i = 1
    while not test_basic(n):
        q = basic(4)
        n = 2*q + 1
        i = root(n)

    salt = random.getrandbits(3)
    secret_key = hash(str(salt) + pswd)
    server_verifier = pw(i, secret_key, n)

    a = random.randint(2, 100)
    A = pw(i, a, n)
    if A != 0:
        b = random.randint(2, 100)
        k = 3
        B = (k * server_verifier + pw(i, b, n)) % n
        if B != 0:
            u = hash(hex(A + B))
            if u != 0:
                client_sk = pw((B - k * pw(i, secret_key, n)), (a + u * secret_key), n)
                client_ek = hash(hex(client_sk))

                server_sk = pw((A * (pw(server_verifier, u, n))), b, n)
                server_ek = hash(hex(server_sk))

                if client_ek == server_ek:
                    print("Ключ сессии на сервере: \t", server_sk)
                    print("Ключ кодирования на сервере: \t", server_ek)
                    print("Ключ сессии на клиенте: \t", client_sk)
                    print("Ключ кодирования на клиенте: \t", client_ek)
                    return server_ek

def basic(i: int) -> int:
    while True:
        r_start = int("1" + "0" * (i), 2)
        r_end = int("1" + "1" * (i), 2)
        num = random.randint(r_start, r_end)
        if test_basic(num):
            return num

def test_basic(n: int) -> bool:
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True

def root(m: int) -> int:
    req = set(num for num in range(1, m) if gcd(num, m) == 1)
    for i in range(1, m):
        act = set(pow(i, powers) % m for powers in range(1, m))
        if req == act:
            return i

def pw(base, exp, mod):
    if exp == 0:
        return 1
    if exp & 1 == 0:
        r = pw(base, exp // 2, mod)
        return (r * r) % mod
    else:
        return (base % mod * pw(base, exp - 1, mod)) % mod

def hash(val: str) -> int:
    return int(hashlib.sha256(val.encode('utf-8')).hexdigest(), 16)

print(SRP('3543'))