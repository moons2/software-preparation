"""
https://www.techiedelight.com/find-kth-largest-element-array/

input:
arr = [7, 4, 6, 3, 9, 1]
k = 2

output:
7

process:
	.	listen to carefully
	I.	clarification questions
	II.	speak your solution logic out load
	III. code
	IV.	runtime analysis
	V.	table test

approach I.
sorting the input not ascending and retrieve the
(n-1) item from the vector.
this approach would take O(nlog(n)) runtime

arr = [7, 4, 6, 3, 9, 1]
		              ^
min-heap = [:k-1]

heap = [7, 9]
		^

the operation to heapify down a tree takes O(lon(n)), which is the worst
case, where the entire tall tree must be iterated. The main idea
of this algorithm is to stablish a vector of size k
and sorting it while it is feeded whit the biggest items
so in the end of the iteration it's guaranteed that the
heap[0] item is the k-th largest element

the runtime analysis of this algorithm is
time: O(nlog(k))
space: O(k)
"""

import heapq
 
# Function to find the k'th largest element in a list using min-heap
def find_kth_largest(ints, k):
 
    # base case
    if not ints or len(ints) < k:
        exit(-1)
 
    # build a min-heap from the first `k` elements in the list
    pq = ints[0:k]
    heapq.heapify(pq)
 
    # do for remaining list elements
    for i in range(k, len(ints)):
        # if the current element is more than the root of the heap
        if ints[i] > pq[0]:
            # replace root with the current element
            heapq.heapreplace(pq, ints[i])
 
    # return the root of min-heap
    return pq[0]
 
 
if __name__ == '__main__':
 
    ints = [7, 4, 6, 3, 9, 1]
    k = 2
    print('k\'th largest element in the list is', find_kth_largest(ints, k))