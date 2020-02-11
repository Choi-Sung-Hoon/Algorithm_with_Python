import sys
from math import sqrt


# implementation of Sieve of Eratosthenes
def eratosthenes(n):
	sieve = [True for _ in range(n)]
	
	for i in range(2, int(sqrt(n)) + 1):
		if sieve[i]:
			for j in range(i * i, n, i):
				sieve[j] = False
				
	return sieve


# run only once
prime_list = eratosthenes(1000001)

while True:
	n = int(sys.stdin.readline())
	if n == 0:
		break
	found = False
	
	# for linear search
	for a in range(2, n):
		if prime_list[a]:
			b = n - a
			if prime_list[b]:
				found = True
				print("{0} = {1} + {2}".format(n, a, b))
				break
	
	if not found:
		print("Goldbach's conjecture is wrong.")
