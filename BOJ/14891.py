import sys

gear = list()
for i in range(4):
	gear.append(int('0b' + sys.stdin.readline(), 2))
k = int(sys.stdin.readline())
command = [list(map(int, sys.stdin.readline().split())) for i in range(k)]


def turn_counter_clockwise(num):
	a = num
	temp = (a >> 7) & 1
	a <<= 1
	a |= temp
	a &= (1 << 8) - 1
	return a


def turn_clockwise(num):
	a = num
	temp = a & 1
	a >>= 1
	a |= (temp << 7)
	a &= (1 << 8) - 1
	return a


def solution(idx, _clockwise, direction):
	if idx < 0 or idx > 3:
		return
	
	# right traverse
	if direction == 1:
		a = (gear[idx] & (1 << 1)) >> 1
		b = (gear[idx - direction] & (1 << 5)) >> 5
	# left traverse
	elif direction == -1:
		a = (gear[idx] & (1 << 5)) >> 5
		b = (gear[idx - direction] & (1 << 1)) >> 1
	flag = True if a != b else False
	
	if flag:
		solution(idx + direction, not _clockwise, direction)
		
		if _clockwise:
			gear[idx] = turn_clockwise(gear[idx])
		else:
			gear[idx] = turn_counter_clockwise(gear[idx])


for i in range(k):
	start = command[i][0] - 1
	clockwise = True if command[i][1] == 1 else False
	
	# left traverse
	solution(start - 1, not clockwise, -1)
	# right traverse
	solution(start + 1, not clockwise, 1)
	
	if clockwise:
		gear[start] = turn_clockwise(gear[start])
	else:
		gear[start] = turn_counter_clockwise(gear[start])

answer = 0
for i in range(4):
	answer += (gear[i] & (1 << 7)) >> (7 - i)
print(answer)
