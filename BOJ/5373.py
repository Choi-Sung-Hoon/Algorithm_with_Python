import sys


def get_plain_index(p):
	if p == 'U':
		return 0
	elif p == 'L':
		return 1
	elif p == 'F':
		return 2
	elif p == 'R':
		return 3
	elif p == 'B':
		return 4
	elif p == 'D':
		return 5


def rotate(p, d):
	global cube
	idx = get_plain_index(p)
	
	if d == '-':
		# rotate plain
		cube[idx] = list(reversed(list(map(list, zip(*cube[idx])))))
		
		if p == 'U':
			cube[1][0], cube[2][0], cube[3][0], cube[4][0] = cube[4][0], cube[1][0], cube[2][0], cube[3][0]
		elif p == 'D':
			cube[1][2], cube[2][2], cube[3][2], cube[4][2] = cube[2][2], cube[3][2], cube[4][2], cube[1][2]
		elif p == 'F':
			temp = cube[0][2]
			cube[0][2] = list(map(list, zip(*cube[3])))[0]
			cube[3][0][0], cube[3][1][0], cube[3][2][0] = list(reversed(cube[5][0]))
			cube[5][0] = list(map(list, zip(*cube[1])))[2]
			cube[1][0][2], cube[1][1][2], cube[1][2][2] = list(reversed(temp))
		elif p == 'B':
			temp = cube[0][0]
			cube[0][0] = list(reversed(list(zip(*cube[1]))[0]))
			cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[5][2]
			cube[5][2] = list(reversed(list(zip(*cube[3]))[2]))
			cube[3][0][2], cube[3][1][2], cube[3][2][2] = temp
		elif p == 'L':
			temp = list(zip(*cube[0]))[0]
			cube[0][0][0], cube[0][1][0], cube[0][2][0] = list(map(list, zip(*cube[2])))[0]
			cube[2][0][0], cube[2][1][0], cube[2][2][0] = list(map(list, zip(*cube[5])))[0]
			cube[5][0][0], cube[5][1][0], cube[5][2][0] = list(reversed(list(zip(*cube[4]))[2]))
			cube[4][0][2], cube[4][1][2], cube[4][2][2] = list(reversed(temp))
		elif p == 'R':
			temp = list(map(list, zip(*cube[0])))[2]
			cube[0][0][2], cube[0][1][2], cube[0][2][2] = list(reversed(list(zip(*cube[4]))[0]))
			cube[4][0][0], cube[4][1][0], cube[4][2][0] = list(reversed(list(zip(*cube[5]))[2]))
			cube[5][0][2], cube[5][1][2], cube[5][2][2] = list(map(list, zip(*cube[2])))[2]
			cube[2][0][2], cube[2][1][2], cube[2][2][2] = temp
	elif d == '+':
		# rotate plain
		cube[idx] = list(map(list, zip(*reversed(cube[idx]))))
		
		if p == 'U':
			cube[1][0], cube[2][0], cube[3][0], cube[4][0] = cube[2][0], cube[3][0], cube[4][0], cube[1][0]
		elif p == 'D':
			cube[1][2], cube[2][2], cube[3][2], cube[4][2] = cube[4][2], cube[1][2], cube[2][2], cube[3][2]
		elif p == 'F':
			temp = cube[0][2]
			cube[0][2] = list(reversed(list(zip(*cube[1]))[2]))
			cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[5][0]
			cube[5][0] = list(reversed(list(zip(*cube[3]))[0]))
			cube[3][0][0], cube[3][1][0], cube[3][2][0] = temp
		elif p == 'B':
			temp = cube[0][0]
			cube[0][0] = list(map(list, zip(*cube[3])))[2]
			cube[3][0][2], cube[3][1][2], cube[3][2][2] = list(reversed(cube[5][2]))
			cube[5][2] = list(map(list, zip(*cube[1])))[0]
			cube[1][0][0], cube[1][1][0], cube[1][2][0] = list(reversed(temp))
		elif p == 'L':
			temp = list(map(list, zip(*cube[0])))[0]
			cube[0][0][0], cube[0][1][0], cube[0][2][0] = list(reversed(list(zip(*cube[4]))[2]))
			cube[4][0][2], cube[4][1][2], cube[4][2][2] = list(reversed(list(zip(*cube[5]))[0]))
			cube[5][0][0], cube[5][1][0], cube[5][2][0] = list(map(list, zip(*cube[2])))[0]
			cube[2][0][0], cube[2][1][0], cube[2][2][0] = temp
		elif p == 'R':
			temp = list(zip(*cube[0]))[2]
			cube[0][0][2], cube[0][1][2], cube[0][2][2] = list(map(list, zip(*cube[2])))[2]
			cube[2][0][2], cube[2][1][2], cube[2][2][2] = list(map(list, zip(*cube[5])))[2]
			cube[5][0][2], cube[5][1][2], cube[5][2][2] = list(reversed(list(zip(*cube[4]))[0]))
			cube[4][0][0], cube[4][1][0], cube[4][2][0] = list(reversed(temp))


# for all test cases
t = int(sys.stdin.readline())
for _ in range(t):
	cube = [
		[['w' for c in range(3)] for r in range(3)],
		[['g' for c in range(3)] for r in range(3)],
		[['r' for c in range(3)] for r in range(3)],
		[['b' for c in range(3)] for r in range(3)],
		[['o' for c in range(3)] for r in range(3)],
		[['y' for c in range(3)] for r in range(3)],
	]

	# for all operations
	n = int(sys.stdin.readline().strip())
	command_list = sys.stdin.readline().strip().split()
	for command in command_list:
		plain, direction = map(str, [c for c in command])
		rotate(plain, direction)

	for r in cube[0]:
		print(''.join(r))
