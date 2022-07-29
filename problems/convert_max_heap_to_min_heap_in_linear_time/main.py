"""
https://www.techiedelight.com/convert-max-heap-min-heap-linear-time/

Given an array representing an max heap, convert to min heap in
linear time and in-place

arr = [1,3,15,4,10,2,5]
	   ^

smallst: 2
conv i: 0


				1
		3 				2
	4		10		15 		5
		
"""

class Solution():

	def LEFT(self, i):
		return 2*i + 1

	def RIGHT(self, i):
		return 2*i + 2

	def swap(self, heap, i, j):
		heap[i], heap[j] = heap[j], heap[i]

	# this operation is log(n), and it is called (len(heap)-2)//2 times, so
	# the runtime of this algorithm is nor linear, but i x log(n)
	def heapify_down(self, heap, i):
		left = self.LEFT(i)
		right = self.RIGHT(i)

		smallest = i
		if i < len(heap) and heap[right] < heap[smallest]:
			smallest = right
		if i < len(heap) and heap[left] < heap[smallest]:
			smallest = left

		if smallest != i:
			self.swap(heap, smallest, i)
			self.heapify_down(heap, smallest)

	def convert(self, heap):
		i = (len(heap)-2)//2
		while i >= 0:
			heapify_down(heap, i)
			i = i-1

	def convertMaxHeap2MinHeap(self, maxHeap):




