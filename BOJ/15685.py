import sys
n = int(sys.stdin.readline())
dragon_curves = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

visited = set()
directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
for c, r, d, g in dragon_curves:
	moves = list()
	moves.append(d)
	# for each generation
	for i in range(g):
		# append reversed element of movements
		for move in moves[::-1]:
			next_move = (move + 1) % 4
			moves.append(next_move)
	
	# check coordination of all movements of dragon curve
	cur_r, cur_c = r, c
	visited.add((cur_r, cur_c))
	for move in moves:
		next_r = cur_r + directions[move][0]
		next_c = cur_c + directions[move][1]
		visited.add((next_r, next_c))
		cur_r, cur_c = next_r, next_c

# check square
answer = 0
for i in range(101):
	for j in range(101):
		if (i, j) in visited and (i, j + 1) in visited and (i + 1, j) in visited and (i + 1, j + 1) in visited:
			answer += 1
print(answer)
