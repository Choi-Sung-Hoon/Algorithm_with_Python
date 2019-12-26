import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
a, b, c, d = map(int, sys.stdin.readline().split())
max_num, min_num = -sys.maxsize + 1, sys.maxsize


def solution(num, i, add, minus, multiply, divide):
	global n, max_num, min_num
	if i == n:
		max_num = max(max_num, num)
		min_num = min(min_num, num)
		return
	else:
		if add:
			solution(num + num_list[i], i + 1, add - 1, minus, multiply, divide)
		if minus:
			solution(num - num_list[i], i + 1, add, minus - 1, multiply, divide)
		if multiply:
			solution(num * num_list[i], i + 1, add, minus, multiply - 1, divide)
		if divide:
			solution(int(num / num_list[i]), i + 1, add, minus, multiply, divide - 1)


solution(num_list[0], 1, a, b, c, d)
print(max_num)
print(min_num)

print(-3 / 4)
print(int(-3 / 4))
print(-3 // 4)
