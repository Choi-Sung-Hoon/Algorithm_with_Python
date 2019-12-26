import sys
from queue import Queue
from copy import deepcopy

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for r in range(n)]

def moveBoard(direction, original_board):
	ret = 0
	temp_board = deepcopy(original_board)
	block_list = list()
	
	# up
	if direction == 0:
		for j in range(n):
			for i in range(n - 1, -1, -1):
				# add non-zero blocks to the stack from the bottom
				if temp_board[i][j] != 0:
					block_list.append(temp_board[i][j])
					temp_board[i][j] = 0
				
			# merge continuous same blocks in the list
			length = len(block_list)
			idx = length - 1
			while idx > -1:
				if idx > 0:
					if block_list[idx] == block_list[idx - 1]:
						block_list[idx - 1:idx + 1] = [block_list[idx] * 2]
						length -= 1
					else:
						idx += 1
				idx -= 2
			
			# arrange blocks in the list from the top
			idx = 0
			while block_list:
				temp_board[idx][j] = block_list.pop()
				idx += 1
	# right
	elif direction == 1:
		for i in range(n):
			for j in range(n):
				# add non-zero blocks to the stack from the left
				if temp_board[i][j] != 0:
					block_list.append(temp_board[i][j])
					temp_board[i][j] = 0
			
			# merge continuous same blocks in the list
			length = len(block_list)
			idx = length - 1
			while idx > -1:
				if idx > 0:
					if block_list[idx] == block_list[idx - 1]:
						block_list[idx - 1:idx + 1] = [block_list[idx] * 2]
						length -= 1
					else:
						idx += 1
				idx -= 2
			
			# arrange blocks in the list from the right
			idx = n - 1
			while block_list:
				temp_board[i][idx] = block_list.pop()
				idx -= 1
	# down
	elif direction == 2:
		for j in range(n):
			for i in range(n):
				# add non-zero blocks to the stack from the top
				if temp_board[i][j] != 0:
					block_list.append(temp_board[i][j])
					temp_board[i][j] = 0
			
			# merge continuous same blocks in the list
			length = len(block_list)
			idx = length - 1
			while idx > -1:
				if idx > 0:
					if block_list[idx] == block_list[idx - 1]:
						block_list[idx - 1:idx + 1] = [block_list[idx] * 2]
						length -= 1
					else:
						idx += 1
				idx -= 2
			
			# arrange blocks in the list from the bottom
			idx = n - 1
			while block_list:
				temp_board[idx][j] = block_list.pop()
				idx -= 1
	# left
	else:
		for i in range(n):
			for j in range(n - 1, -1, -1):
				# add non-zero blocks to the stack from the right
				if temp_board[i][j] != 0:
					block_list.append(temp_board[i][j])
					temp_board[i][j] = 0
			
			# merge continuous same blocks in the list
			length = len(block_list)
			idx = length - 1
			while idx > -1:
				if idx > 0:
					if block_list[idx] == block_list[idx - 1]:
						block_list[idx - 1:idx + 1] = [block_list[idx] * 2]
						length -= 1
					else:
						idx += 1
				idx -= 2
			
			# arrange blocks in the list from the left
			idx = 0
			while block_list:
				temp_board[i][idx] = block_list.pop()
				idx += 1
	
	# find maximum block
	for i in range(n):
		for j in range(n):
			if temp_board[i][j] > ret:
				ret = temp_board[i][j]
	return temp_board, ret


def solution():
	q = Queue()
	q.put((board, 0))
	visited = list()
	answer = 0
	
	while q.qsize() > 0:
		original_board, count = q.get()
		
		if count > 4:
			return answer
		
		for i in range(4):
			temp_board, ret = moveBoard(i, original_board)
			
			if ret > answer:
				answer = ret
			
			if temp_board not in visited:
				q.put((temp_board, count + 1))
		visited.append(original_board)
		
	return answer


print(solution())
