'''
https://www.techiedelight.com/find-kth-smallest-element-array/

Given an integer array, find k'th smallest element in the 
array where k is a positive integer less than or 
equal to the length of array.

Input:
 
arr = [7, 4, 6, 3, 9, 1]
k = 3
 
Output:
 
k’th smallest array element is 4

.	listen to carefully
I.	clarification questions
II.	speak your solution logic out loud
III.runtime analysis
IV.	code
V.	table test

A first approach would be sort the arr in ascending
order and get the k'th item from list. But this 
woul easily take O (N log(N)), where N is the input size

But we can improve this complexity

arr 	[7, 4, 6, 3, 9, 1]
		                ^

pq(k)	[4, 1, 3]
pop
insert
heapify

So the idea is to iterate over arr with a 
window of size k, heapifying max this window
by the end of arr, the item with
high priority will be the k'th item from
the pq is feeded only if arr[i] < pq[0]

TEST

k: 1
input:	[7, 4, 6]
			   ^

maxpq:	[4]

should I return the item or the index of the Item?
'''

import heapq

def findKthSmallestElement(arr, k):

	if not len(arr):
		# what should I return in case of
		# arr empty ?
		pass

	pq = arr[0:k]
	heapq._heapify_max(pq)

	for item in arr[k:]:
		if item < pq[0]:
			pq[0] = item
			heapq._heapify_max(pq)

	print (f'{k}"th element is {pq[0]}')



if __name__ == '__main__':
	findKthSmallestElement([7, 4, 6, 3, 9, 1], 2)