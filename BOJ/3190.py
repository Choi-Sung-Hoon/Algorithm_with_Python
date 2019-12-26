import sys
from queue import Queue

n = int(sys.stdin.readline())
board = list([[0, 0] for c in range(n + 1)] for r in range(n + 1))
k = int(sys.stdin.readline())
apple_list = set(tuple(map(int, sys.stdin.readline().split())) for i in range(k))
l = int(sys.stdin.readline())
action_list = Queue()
for i in range(l):
	x, c = sys.stdin.readline().split()
	action_list.put((int(x), c))

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
head, tail = (1, 1), (1, 1)
head_dir, tail_dir = 1, 1
board[1][1] = [1, 1]
cur_time = 0
next_time, move = action_list.get()
while True:
	dr = directions[head_dir][0]
	dc = directions[head_dir][1]
	next_r = head[0] + dr
	next_c = head[1] + dc
	
	# if snake's head meet the wall or its body
	if next_r <= 0 or next_r > n or next_c <= 0 or next_c > n or board[next_r][next_c][0] == 1:
		break

	# if there's an apple at the next position
	if (next_r, next_c) in apple_list:
		# record the direction of head
		board[head[0]][head[1]][1] = head_dir
		# eat apple
		apple_list.remove((next_r, next_c))
	# if there's no apple
	else:
		board[tail[0]][tail[1]][0] = 0
		# shorten the snake's length by moving tail
		tail_dir = board[tail[0]][tail[1]][1]
		dr = directions[tail_dir][0]
		dc = directions[tail_dir][1]
		tail = (tail[0] + dr, tail[1] + dc)
	# extend the snake's length
	head = (next_r, next_c)
	board[next_r][next_c] = [1, head_dir]
	
	# handling next action
	cur_time += 1
	if cur_time == next_time:
		if move == 'L':
			head_dir = (head_dir + 3) % 4
		elif move == 'D':
			head_dir = (head_dir + 1) % 4
		board[head[0]][head[1]][1] = head_dir
		if action_list.qsize() > 0:
			next_time, move = action_list.get()

print(cur_time + 1)
