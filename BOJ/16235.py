import sys

inputLine = sys.stdin.readline().split()
n, m, k = int(inputLine[0]), int(inputLine[1]), int(inputLine[2])

field = [[5 for r in range(n + 1)] for c in range(n + 1)]
trees = [[list() for r in range(n + 1)] for c in range(n + 1)]
A = [[0 for r in range(n + 1)] for c in range(n + 1)]

for r in range(1, n + 1):
	inputLine = sys.stdin.readline().split()
	for c in range(1, n + 1):
		A[r][c] = int(inputLine[c - 1])
		
for i in range(m):
	r, c, age = list(map(int, sys.stdin.readline().split()))
	trees[r][c].append(age)
	
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

for year in range(k):
	dead_trees = list()
	# spring & summer
	for r in range(1, n + 1):
		for c in range(1, n + 1):
			temp = 0
			for i in range(len(trees[r][c]) - 1, -1, -1):
				if field[r][c] >= trees[r][c][i]:
					field[r][c] -= trees[r][c][i]
					trees[r][c][i] += 1
				else:
					temp += trees[r][c][i] // 2
					trees[r][c].pop(i)
			field[r][c] += temp

	# autumn
	for r in range(1, n + 1):
		for c in range(1, n + 1):
			for i, age in enumerate(trees[r][c]):
				if age % 5 == 0:
					# for all directions
					for direction in range(8):
						new_r = r + dr[direction]
						new_c = c + dc[direction]
						if 1 <= new_r <= n and 1 <= new_c <= n:
							trees[new_r][new_c].append(1)
			# winter
			field[r][c] += A[r][c]

count = 0
for r in range(1, n + 1):
	for c in range(1, n + 1):
		count += len(trees[r][c])
print(count)
