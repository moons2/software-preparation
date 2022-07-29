'''
Bubble sort is the most simple and easy sorting algorithm
recomended for small datasets
its main idea is making comparisons among the n elements
with (n-1), hence, its time complexity is O(n^2) and
its space complexity is O(n)
'''
def BubbleSort():
	arr = [int(i) for i in input().split(" ")]

	# corner case para arr vazio
	if not len(arr):
		return -1

	# corner case para array unitario
	if len(arr) == 1:
		return arr

	size = len(arr) - 1

	for i in range(size, -1, -1):
		smaller = i
		for j in range(i-1, -1, -1):
			if(arr[j] > arr[smaller]):
				smaller = j
		arr[i], arr[smaller] = arr[smaller], arr[i]

	print(arr)

if __name__ == '__main__':
	BubbleSort()