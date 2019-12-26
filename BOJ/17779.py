import sys

n = int(sys.stdin.readline())
A = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for r in range(1, n + 1, 1):
	line = list(map(int, sys.stdin.readline().split()))
	for c in range(1, n + 1, 1):
		A[r][c] = line[c - 1]


def solution(x, y, d1, d2):
	max_sum, min_sum = 0, sys.maxsize
	temp_board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
	
	# border 1
	for d in range(0, d1 + 1, 1):
		temp_board[x + d][y - d] = 5
	
	# border 2
	for d in range(0, d2 + 1, 1):
		temp_board[x + d][y + d] = 5
	
	# border 3
	for d in range(0, d2 + 1, 1):
		temp_board[x + d1 + d][y - d1 + d] = 5
	
	# border 4
	for d in range(0, d1 + 1, 1):
		temp_board[x + d2 + d][y + d2 - d] = 5
	
	# sum of sector 1
	sum1 = 0
	for i in range(1, x + d1):
		for j in range(1, y + 1, 1):
			if temp_board[i][j] == 5:
				break
			sum1 += A[i][j]
	max_sum = max(max_sum, sum1)
	min_sum = min(min_sum, sum1)
		
	# sum of sector 2
	sum2 = 0
	for i in range(x + d2, 0, -1):
		for j in range(n, y, -1):
			if temp_board[i][j] == 5:
				break
			sum2 += A[i][j]
	max_sum = max(max_sum, sum2)
	min_sum = min(min_sum, sum2)
		
	# sum of sector 3
	sum3 = 0
	for i in range(x + d1, n + 1, 1):
		for j in range(1, y - d1 + d2, 1):
			if temp_board[i][j] == 5:
				break
			sum3 += A[i][j]
	max_sum = max(max_sum, sum3)
	min_sum = min(min_sum, sum3)
		
	# sum of sector 4
	sum4 = 0
	for i in range(n, x + d2, -1):
		for j in range(n, y - d1 + d2 - 1, -1):
			if temp_board[i][j] == 5:
				break
			sum4 += A[i][j]
	max_sum = max(max_sum, sum4)
	min_sum = min(min_sum, sum4)
	
	# sum of sector 5
	sum5 = total - (sum1 + sum2 + sum3 + sum4)
	max_sum = max(max_sum, sum5)
	min_sum = min(min_sum, sum5)
	
	return max_sum - min_sum


total = sum(map(sum, A))
answer = total
for r in range(1, n + 1, 1):
	for c in range(1, n + 1, 1):
		for d1 in range(1, n + 1, 1):
			for d2 in range(1, n + 1, 1):
				if 1 < r + d1 + d2 <= n and 1 <= c - d1 < c + d2 <= n:
					answer = min(answer, solution(r, c, d1, d2))
print(answer)
