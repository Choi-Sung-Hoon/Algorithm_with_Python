import sys
from queue import Queue

n, m = map(int, sys.stdin.readline().split())
board = [[0 for c in range(m)] for r in range(n)]
R = (0, 0)
B = (0, 0)
EXIT = (0, 0)

for i in range(n):
	line = sys.stdin.readline()
	for j in range(m):
		board[i][j] = line[j]
		
		if board[i][j] == 'R':
			R = (i, j)
		elif board[i][j] == 'B':
			B = (i, j)
		elif board[i][j] == 'O':
			EXIT = (i, j)

# N, E, S, W
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution():
	# BSF
	q = Queue()
	q.put((R, B, 0))
	visited = dict()
	
	while q.qsize() > 0:
		red, blue, count = q.get()
		
		# termination condition
		if count > 10:
			return -1
		
		for dr, dc in directions:
			# move blue ball
			dist_blue = 0
			next_blue = blue
			while board[next_blue[0] + dr][next_blue[1] + dc] != 'O' and board[next_blue[0] + dr][next_blue[1] + dc] != '#':
				next_blue = (next_blue[0] + dr, next_blue[1] + dc)
				dist_blue += 1
				
			# move red ball
			dist_red = 0
			next_red = red
			while board[next_red[0] + dr][next_red[1] + dc] != 'O' and board[next_red[0] + dr][next_red[1] + dc] != '#':
				next_red = (next_red[0] + dr, next_red[1] + dc)
				dist_red += 1
			
			# blue ball is out
			if board[next_blue[0] + dr][next_blue[1] + dc] == 'O':
				continue
			elif board[next_red[0] + dr][next_red[1] + dc] == 'O':
				return count + 1
			
			# if the balls are at the same position
			if next_blue == next_red:
				if dist_red > dist_blue:
					next_red = (next_red[0] - dr, next_red[1] - dc)
				elif dist_red < dist_blue:
					next_blue = (next_blue[0] - dr, next_blue[1] - dc)
			
			# prevent count from being over 10
			if count == 10:
				return -1
			
			if (next_red, next_blue) not in visited:
				q.put((next_red, next_blue, count + 1))
		visited[(red, blue)] = True
	return -1


print(solution())
