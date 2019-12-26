from collections import Counter


def solution(clothes):
	answer = 0
	
	# make categories dictionary
	categories = list()
	for name, category in clothes:
		categories.append(category)
	categories = Counter(categories)
	
	length = len(categories.values())
	# if there's only one category
	if length == 1:
		answer = list(categories.values())[0]
	# if there are one more category
	elif length > 1:
		temp = 1
		for value in list(categories.values()):
			# get the combination including the case of NOT wearing an item
			temp *= (value + 1)
		answer += temp - 1
	
	return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
