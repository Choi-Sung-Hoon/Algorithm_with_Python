def solution(participant, completion):
	answer = ''
	
	# for all players, count every different name
	participant_dict = dict()
	for player in participant:
		if player not in participant_dict:
			participant_dict[player] = 1
		else:
			participant_dict[player] += 1
	
	# count who completed the marathon
	for player in completion:
		participant_dict[player] -= 1
	
	# find who didn't complete the marathon yet
	for player in participant_dict:
		if participant_dict[player] == 1:
			answer = player
			break
		
	return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
