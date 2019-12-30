def solution(arrangement):
	answer = 0
	replaced = arrangement.replace('()', '.')
	stack = list()
	
	for i, c in enumerate(replaced):
		if c == '(':
			stack.append(c)
			answer += 1
		elif c == ')':
			stack.pop()
		else:
			answer += len(stack)
	
	return answer

print(solution("()(((()())(())()))(())"))
