import random
import math


class Deff(object):
    def __init__(self, name, length):
        self.name = name
        self.pb_alice = basic(length)
        self.pb_dean = basic(length)
        self.pr_key = basic(length)
        self.full_key = None

    def gen_part(self):
        res = self.pb_alice ** self.pr_key % self.pb_dean
        print(f"Generate partial key for {self.name}\t{res} =", self.pb_alice, "^", self.pr_key, "mod", self.pb_dean)
        return res

    def gen_full(self, partial):
        self.full_key = partial ** self.pr_key % self.pb_dean
        print(f"Generate full key for {self.name}\t{self.full_key} =", partial, "^", self.pr_key, "mod", self.pb_dean)

    def encode(self, message):
        return "".join([chr(ord(c) ^ self.full_key) for c in message])

def basic(n: int) -> int:
    while True:
        r_start = int("1" + "0" * (n), 2)
        r_end = int("1" + "1" * (n), 2)
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

def exchange(alice, dean, sam: Deff):
    alice.pb_dean = dean.pb_dean
    dean.pb_alice = alice.pb_alice
    sam.pb_alice = alice.pb_alice

def gen_full(alice, dean, sam: Deff):
    a_partial = alice.gen_part()
    d_partial = dean.gen_part()
    s_partial = sam.gen_part()
    alice.gen_full(d_partial)
    dean.gen_full(a_partial)
    sam.gen_full(a_partial)


message = "Фамилия Остапенко выграверована на мемореале в Севастополе 26 раз"
length = int(math.log2(max([ord(c) for c in message])))

Alice = Deff("Alice", length)
Dean = Deff("Dean", length)
Sam = Deff("Sam", length)

print(f"Alice keys\t public {Alice.pb_alice}, \tprivate {Alice.pr_key}")
print(f"Dean keys\t  public {Dean.pb_dean}, \tprivate {Dean.pr_key}")

exchange(Alice, Dean, Sam)
print("Public key exchange")
gen_full(Alice, Dean, Sam)
b_encrypted = Dean.encode(message)
print("Encrypted\n\t", b_encrypted)

desc_message = Alice.encode(b_encrypted)
print("Deciphered\n\t", desc_message)
desc_message = Sam.encode(b_encrypted)
print("Deciphered\n\t", desc_message)