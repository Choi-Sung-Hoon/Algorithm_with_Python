from operator import itemgetter


def solution(genres, plays):
	answer = []
	
	total_plays = dict()
	songs = dict()
	for i, genre in enumerate(genres):
		# count total plays for each genre
		if genre not in total_plays:
			total_plays[genre] = 0
		total_plays[genre] += plays[i]
		# add current song to hash map
		if genre not in songs:
			songs[genre] = list()
		songs[genre].append((i, plays[i]))
	
	# sort genres by total plays
	sorted_total_plays = sorted(total_plays.items(), key=itemgetter(1), reverse=True)
	# sort songs in a genre by its plays
	for genre in songs:
		songs[genre].sort(key=itemgetter(1), reverse=True)

	# make best album
	for genre, total_plays in sorted_total_plays:
		if len(songs[genre]) > 1:
			candidates = list(zip(songs[genre][0], songs[genre][1]))[0]
			answer.extend(candidates)
		else:
			candidate = songs[genre][0][0]
			answer.append(candidate)
			
	return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
