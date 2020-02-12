import sys

dwarf_list = [int(sys.stdin.readline()) for _ in range(9)]
dwarf_check = [0 for _ in range(9)]
answer = []


def dfs(n, count, sum_height):
	if n == 9:
		if count == 7 and sum_height == 100:
			for idx, v in enumerate(dwarf_check):
				if v:
					answer.append(dwarf_list[idx])
			
			print(*sorted(answer), sep='\n')
			sys.exit(0)
		return

	# select a dwarf
	dwarf_check[n] = 1
	dfs(n + 1, count + 1, sum_height + dwarf_list[n])
	
	# don't select a dwarf
	dwarf_check[n] = 0
	dfs(n + 1, count, sum_height)


dfs(0, 0, 0)
