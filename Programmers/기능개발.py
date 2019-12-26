from collections import deque


def solution(progresses, speeds):
	answer = []
	
	q = deque(progresses)
	speeds = deque(speeds)
	while q:
		count = 0
		
		# make progress
		for i, speed in enumerate(speeds):
			q[i] += speed
		
		# if the first job can be released
		if q[0] > 100:
			# release and count progresses continuously
			while q and q[0] > 100:
				q.popleft()
				speeds.popleft()
				count += 1

		# if there's a released progress
		if count:
			answer.append(count)
			
	return answer
	
	
print(solution([93,30,55], [1,30,5]))
