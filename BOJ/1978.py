import sys
from math import sqrt

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))


def is_prime(value):
	if value == 1:
		return False
	
	for i in range(2, int(sqrt(value) + 1)):
		if value % i == 0:
			return False
		
	return True


answer = 0
for i in numbers:
	if is_prime(i):
		answer += 1
print(answer)
