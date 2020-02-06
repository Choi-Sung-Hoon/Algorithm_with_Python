import sys
from math import gcd

t = int(sys.stdin.readline())
for _ in range(t):
	line = list(map(int, sys.stdin.readline().split()))
	n, numbers = line[0], line[1:]
	
	answer = 0
	for i in range(n - 1):
		for j in range(i + 1, n):
			answer += gcd(numbers[i], numbers[j])
	print(answer)
