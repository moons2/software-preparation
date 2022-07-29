'''
https://www.techiedelight.com/merge-m-sorted-lists-variable-length/

Input:  4 sorted lists of variable length
 
[10, 20, 30, 40]
[15, 25, 35]
[27, 29, 37, 48, 93]
[32, 33]
 
Output:
 
[10, 15, 20, 25, 27, 29, 30, 32, 33, 35, 37, 40, 48, 93]

.	listen to carefully
I.	clarification questions
II.	speak your logic solution out loud
III.code
IV.	runtime analysis
V.	Desk test

I.	
	.	What should I return in case sorted lists be empty?

	.	must the final array be in place or can I create another variable
	to hold the result?


Input:
		[10]
		  ^
		[15, 25, 35]
		  	 ^
		[27, 29, 37, 48, 93]
		  ^
		[32, 33]
		  ^

heap:	[20, 25, 27, 32]

Output:
res:	[10, 15, 27, 32]
		 ^

RUNTIME ANALYSIS
TIME:		O(M log(k)), para M = soma de itens das listas, k número de listas
SPACE:		O(k), devido a utilização de k nós para o manuseio da heap
'''


import heapq

# A utilidade desta classe está em
# gerenciar o estado de qual valor foi removido
# para saber de qual lista obter o proximo item
class Node():
	def __init__(self, value, list_index, value_index):
		self.value = value
		self.list_index = list_index
		self.value_index = value_index

	def info(self):
		print(f"{self.value}, {self.list_index}, {self.value_index}")

	def __lt__(self, other):
		return self.value < other.value

class Solution():
	def sortSortedArrays(self, lists):

		if not lists:
			# what should I return in case of lists
			# be empty?
			pass

		pq = [Node(lists[i][0], i, 0) for i in range(len(lists)) if len(lists[i]) > 0]

		# while pq is not empty
		while (pq):
			# pop the Node with highest priority
			# in this case that one with the
			# lowest value
			heapq.heapify(pq)
			min_node = heapq.heappop(pq)
			min_node.info()

			# [0,1]
			if min_node.value_index + 1 < len(lists[min_node.list_index]):
				pq.append(Node(lists[min_node.list_index][min_node.value_index+1], min_node.list_index, min_node.value_index+1))


if __name__ == '__main__':
	lists=[[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]]
	Solution().sortSortedArrays(lists)