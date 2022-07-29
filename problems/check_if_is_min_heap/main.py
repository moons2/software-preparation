"""
https://www.techiedelight.com/check-given-array-represents-min-heap-not/
Check if an array represents a min-heap or not

# case 1
input:
arr = [2,3,4,5,10,15]

		 __	2 __
	  __3__	    __4__
	 5	  10   15

output:
	true

a min-heap is a priority queue, where each item is smaller than
its child. And the highest priority is the smallest key.

# case 2
input:
arr = [2,10,3,4,5,15]
		 __	2 __
	  __10__    __3__
	 4	   5   15

output:
	false

.	listen to carefully
I.	clarification questions
II.	code
III.runtime analysis
IV.	desk test
V.	

Approach I

input:
	   0,1,2,3,4, 5
arr = [2,3,4,5,10,15]
	     ^
	   left = 2i+1
	   right = 2i+2

we iterate over the arr applying the validation over the children nodes
to validate the min heap property, i.e., if

	arr[i] <= arr[2i+1]
	arr[i] <= arr[2i+2]
"""

class Solution():
	def isMinHeap(self, arr):

		if not arr:
			# what should I return if arr were empty?
			return None

		arrSize = len(arr)
		for i in range(arrSize):
			# Numa min heap o pai deve ser menor que o
			if 2*i+1 < arrSize and arr[i] > arr[2*i+1]:
				return False
			if 2*i+2 < arrSize and arr[i] > arr[2*i+2]:
				return False

		return True

if __name__ == "__main__":
	solution = Solution()
	arr = [2,3,4,5,10,15]

	print(arr)
	print(solution.isMinHeap(arr))


