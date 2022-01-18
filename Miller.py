import random


def Miller(d, n):
	#n>4
	a = 2 + random.randint(1, n - 4)
	#a^d % n
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


#(x^y) % p
def pw(x, y, p):
	res = 1
	#Если x>p, то значение x = остатку от деления от p
	x = x % p
	while (y > 0):
		if y & 1:
			res = (res * x) % p
		y = y >> 1
		x = (x * x) % p
	return res


def prime(n, k):
	#Край
	if (n <= 1 or n == 4):
		return False
	if (n <= 3):
		return True
    #r, при n = 2^d * r + 1, где r >=1
	d = n - 1
	while (d % 2 == 0):
		d //= 2
	# k - итерации теста Миллера
	for i in range(k):
		if (Miller(d, n) == False):
			return False
	return True


number = int(input('Введите число: '))
k = int(input('Введите количество итераций:'))
print(prime(number, k))

