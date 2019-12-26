import sys

n = int(sys.stdin.readline())
tester = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

answer = 0
for i in range(n):
	tester[i] -= b
	if tester[i] > 0:
		if tester[i] % c == 0:
			answer += 1 + (tester[i] // c)
		else:
			answer += 2 + (tester[i] // c)
	else:
		answer += 1
print(answer)
