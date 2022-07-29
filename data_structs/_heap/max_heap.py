# Implementation of a Max Heap in Python
# according to the version techiedelight.com/min-heap-max-heap-implementation-in-java/
class PriorityQueue():
	# that's a pattern put a single or double underscore
	# in the begining of a variable to be treat as a private variable
	# because python has no private delimiter as other languages
	__heap = None

	def __init__(self):
		self.__heap = []

	# return parent's indice
	def parent(self, i):
		if i == 0:
			return 0

		# floor division
		return (i-1) // 2

	# return right child's indice
	def right(self, i):
		return 2*i + 2

	# return left child's indice
	def left(self, i):
		return 2*i + 1

	# return Heap size
	def size(self):
		return len(self.__heap)

	# highest priority key without change Heap
	def peek(self):
		try:
			if self.isEmpty:
				raise Exception("Heap is empty!")
			return self.__heap[0]
		except Exception as e:
			raise e

	# return highest priority key making change
	def pull(self):
		try:
			if self.isEmpty():
				raise Exception("Heap is empty!") 
			self.swap(0, -1)
			root = self.__heap.pop()
			self.heapify_down(0)
			return root
		except Exception as e:
			raise e

	# insert at the end and call heapify_up
	def add(self, value):
		try:
			self.__heap.append(value)
			self.heapify_up(self.size()-1)
		except Exception as e:
			raise e

	# clear the entire heap
	def clear(self):
		self.__heap = []

	# make swap between values of indices a and b
	def swap(self, a, b):
		self.__heap[a], self.__heap[b] = self.__heap[b], self.__heap[a]

	# check if Heap is empty
	def isEmpty(self):
		return not bool(self.size())

	# check if Heap contains a specified element
	def contains(self, value):
		return value in self.__heap

	# return the entire Heap as an array
	def toArray(self):
		return self.__heap

	# O(log(n)) operation
	# operation that certify the heap property recursively up
	def heapify_up(self, i):
		try:
			if( i > 0 and self.__heap[self.parent(i)] < self.__heap[i]):
				self.swap(i, self.parent(i))
				self.heapify_up(self.parent(i))
		except Exception as e:
			raise e

	# O(log(n)) operation
	# operation that certify the heap property recursively down
	def heapify_down(self, i):
		try:
			RIGHT = right(i)
			LEFT = left(i)
			largest = i

			if (RIGHT < self.size() and self.__heap[RIGHT] > self.__heap[i]):
				largest = RIGHT
			if (LEFT < self.size() and self.__heap[LEFT] < self.__heap[largest]):
				largest = LEFT

			if largest != i:
				self.swap(i, largest)
				self.heapify_down(largest)

		except Exception as e:
			raise e


if __name__ == '__main__':
	Heap = PriorityQueue()
	Heap.add(1)
	Heap.add(6)
	Heap.add(31)
	print(Heap.toArray())