"""
https://www.techiedelight.com/sort-k-sorted-array/

Sort a k-sorted array
Given a k–sorted array that is almost sorted such 
that each of the n elements may be misplaced by no more than k positions 
from the correct sorted order. 
Find a space-and-time efficient algorithm to sort the array.

The work key here is "shifted by k", so to ptimize the sorting
we create a k+1 array and keep them heapifyed.

k = 1
input = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]
		                       [      ]
10
i 	: 9
i+k : 10

heap = [1, 4, 5]

the sorting process takes O(log(k))
and the iteration over the entire input takes O(N)
this way, this algorithm takes
O(Nlog(k))

.	listen to carefully
I.
"""

# package which implements a min heap
# import heapq

def RIGHT(i):
	return 2*i + 2

def LEFT(i):
	return 2*i + 1

def swap(heap, i, j):
	heap[i], heap[j] = heap[j], heap[i]

def heapify_down(heap, i):
	smallest = i
	left = LEFT(i)
	right = RIGHT(i)

	if left < len(heap) and heap[left] < heap[i]:
		smallest = left

	if right < len(heap) and heap[right] < heap[smallest]:
		smallest = right

	if smallest != i:
		swap(heap, smallest, i)
		heapify_down(heap, smallest)

def sortKSortedArray(array, k):
	arrSize = len(array)
	# corner case for empty array
	if not arrSize or k > arrSize:
		exit(-1)

	for i in range(arrSize):
		if i + k >= arrSize:
			k -= 1
		heapify_down(array[i:i+k+1], 0)
		print(array[i:i+k+1])



if __name__ == '__main__':
	arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
	sortKSortedArray(arr, 2)
	print(arr)

# ========== ========== ========== ==========

