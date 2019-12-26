import sys
from collections import Counter

r, c, k = map(int, sys.stdin.readline().strip().split())
A = [[0 for _ in range(101)] for _ in range(101)]
for i in range(3):
	line = list(map(int, sys.stdin.readline().strip().split()))
	for j in range(3):
		A[i][j] = line[j]

answer, max_r, max_c = 0, 3, 3
while A[r - 1][c - 1] != k and answer < 101:
	# operation R
	if max_r >= max_c:
		# for all rows
		for i in range(max_r):
			sorted_row = list(sorted(Counter(A[i]).items(), key=lambda x: (x[1], x[0])))
			
			j = 0
			for key, occurrence in sorted_row:
				if key != 0:
					A[i][j] = key
					A[i][j + 1] = occurrence
					j += 2
			max_c = max(max_c, j)
			# set rest of blanks to 0
			for j in range(j, 101, 1):
				A[i][j] = 0
	# operation C
	else:
		# transposed matrix of A
		transposed_A = list(zip(*A))
		for j in range(max_c):
			sorted_col = list(sorted(Counter(transposed_A[j]).items(), key=lambda x: (x[1], x[0])))
			
			i = 0
			for key, occurrence in sorted_col:
				if key != 0:
					A[i][j] = key
					A[i + 1][j] = occurrence
					i += 2
			max_r = max(max_r, i)
			# set rest of blanks to 0
			for i in range(i, 101, 1):
				A[i][j] = 0
	answer += 1

if answer < 101:
	print(answer)
else:
	print(-1)
