class Node(object):
	def __init__(self, value, end=False):
		self.value = value
		self.children = dict()
		self.end = end


class Trie(object):
	def __init__(self):
		self.root = Node(None)
		
	def insert(self, string):
		cur = self.root
		for c in string:
			if c not in cur.children:
				cur.children[c] = Node(c)
			cur = cur.children[c]
			# if this is the end of the string
			if cur.end:
				return False
		cur.end = True
		return True
		

def solution(phone_book):
	phone_book.sort()
	trie = Trie()
	for phone_number in phone_book:
		if not trie.insert(phone_number):
			return False
	return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
