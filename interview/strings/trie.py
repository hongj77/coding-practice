""" Implementation of trie to autocomplete a word. P.S. Brady zhou """


class Node:

	def __init__(self, val, isLeaf=False):
		self.val = val
		self.isLeaf = isLeaf
		self.children = dict() # dictionary of [character]->Node


class SuffixTree:

	def __init__(self):
		self.root = Node("", False)


	def insert(self, word):
		
		current_node = self.root # start at the root and look down
		last_index = len(word)-1

		for i, char in enumerate(word):

			if i == last_index:			
				if char not in current_node.children:
					current_node.children[char] = Node(char, True)
				else:
					current_node.children[char].isLeaf = True
			else:
				if char not in current_node.children:
					current_node.children[char] = Node(char, False)

			current_node = current_node.children[char]


	def possibleWords(self,pattern):

		def get_paths(result, current_node, path):
			if current_node.isLeaf:
				result.append(path)

			for child_node in current_node.children.values():
				get_paths(result, child_node, path+child_node.val)


		result = []
		current_prefix = ""
		last_index = len(pattern)-1
		current_node = self.root

		for i, char in enumerate(pattern):

			if char not in current_node.children:
				# if pattern doesn't match any word in trie, then can't autocomplete
				break
		
			current_node = current_node.children[char]
			current_prefix += char

			if i == last_index:
				# this is the end of the pattern. Next, get all the possibilities
				get_paths(result, current_node, current_prefix)

		return result



if __name__=="__main__":

	suffix_tree = SuffixTree()

	# populate the tree
	T = int(raw_input())
	for _ in range(T):
		word = raw_input()
		suffix_tree.insert(word)

	print suffix_tree.possibleWords(raw_input())

	# print suffix_tree.possibleWords("")
	# print suffix_tree.possibleWords("br")
	# print suffix_tree.possibleWords("bra")
	# print suffix_tree.possibleWords("brah")
	# print suffix_tree.possibleWords("brady")


