#!/usr/local/bin/python
import sys

class Solution():

	def getDiff(self, str_a, str_b):
		"""
		:type str_a: str
		:type str_b: str
		:rtype: int

		Finds the number of characters that are different in both string
		in position and not absoulte.

		Given both the strings are of same length
		"""
		diff = 0
		for i in xrange(len(str_a)):
			if str_a[i] != str_b[i]:
				diff +=1

		return diff

	def ladderLength(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: int
		"""
		if endWord not in wordList: 
			if self.getDiff(beginWord, endWord) == 1:
				return 1
			else:
				return 0
		elif beginWord in wordList and endWord in wordList and len(wordList) == 2 and self.getDiff(beginWord, endWord) != 1:
			return 0

		graph = dict()
		dist_dict = dict()
		final_dist_dict = dict()
		vertex_predecessors = dict()

		if beginWord not in wordList: 
			wordList.insert(0,beginWord)

		# Formulate the graph (all nodes are connected to each other)
		for i in xrange(len(wordList)):

			vertex = dict()
			dist_dict[wordList[i]] = 999 
			final_dist_dict[wordList[i]] = 999
			vertex_predecessors[wordList[i]] = ''

			for j in xrange(len(wordList)):
				if ( self.getDiff(wordList[i], wordList[j]) == 1 ):
					vertex[wordList[j]] = 1
			graph[wordList[i]] = vertex

		# print(graph)
		
		# Main logic
		start_vertex = beginWord
		dist_dict[start_vertex] = 0 
		final_dist_dict[start_vertex] = 0 
		dist_dict.pop(start_vertex.encode('utf'))
		vertex_predecessors[start_vertex] = ''

		while dist_dict:
			print('Start vertex: ' + start_vertex)

			adj_vertices = graph[start_vertex] # Dict
			# print(adj_vertices.items())
			curr_distance = final_dist_dict[start_vertex]

			if (len(adj_vertices)) < 1: # Last vertex
				break
			for vertex_key,distance in adj_vertices.items():
				if(vertex_key not in dist_dict.keys()):
					continue
				if (distance + curr_distance) < dist_dict[vertex_key]:
					print(vertex_key + str(distance)) 
					dist_dict[vertex_key] = (distance + curr_distance)
					final_dist_dict[vertex_key] = (distance + curr_distance)
			
			# Find the next smallest element
			# Pop out that from dist_dict
			# loop with that as start vertex
			
			# print(dist_dict)
			min_dist = 999
			min_dist_key = ''

			for key, value in dist_dict.items():
				if value < min_dist:
					min_dist = value
					min_dist_key = key

			if min_dist == 999:
				min_dist_key = dist_dict.items()[0][0]		

			dist_dict.pop(min_dist_key)
			vertex_predecessors[min_dist_key] = start_vertex
			start_vertex = min_dist_key

			# print(vertex_predecessors)
		if final_dist_dict[endWord.encode('utf')] == 999:
			return 0
		else:	
			return final_dist_dict[endWord.encode('utf')] + 1

def main():

	
	beginWord = "hit"
	endWord = "cog"
	wordList = ["hot","cog","dot","dog","hit","lot","log"]
	"""
	beginWord = "hot"
	endWord = "dog"
	wordList = ["hot","dog","dot"]

	
	beginWord = "red"
	endWord = "tax"
	wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
	"""
	sol = Solution()
	print(sol.ladderLength(beginWord,endWord,wordList))

if __name__ == '__main__':
	main()