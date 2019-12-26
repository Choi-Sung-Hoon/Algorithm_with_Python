import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
board = [[0 for c in range(n + 1)] for r in range(n + 1)]
house_list = list()
chicken_list = list()
for i in range(1, n + 1, 1):
	line = sys.stdin.readline().split()
	for j in range(1, n + 1, 1):
		board[i][j] = int(line[j - 1])
		if board[i][j] == 1:
			house_list.append((i, j))
		elif board[i][j] == 2:
			chicken_list.append((i, j))

answer = sys.maxsize
for comb in combinations(chicken_list, m):
	city_dist = 0
	for (house_r, house_c) in house_list:
		chicken_dist = sys.maxsize
		for chicken_r, chicken_c in comb:
			dist = abs(chicken_r - house_r) + abs(chicken_c - house_c)
			chicken_dist = min(chicken_dist, dist)
		city_dist += chicken_dist
	answer = min(answer, city_dist)
print(answer)
