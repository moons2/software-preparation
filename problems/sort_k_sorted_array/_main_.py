import heapq


# arr = [4, 1, 5, 2, 3, 7, 8, 6, 10, 9]
#		                     [        ]
#
#

def sort_k_sorted_num(nums, k):
	if not nums or k > len(nums):
		exit(-1)

	for i in range(len(nums)):
		if i + k + 1 == len(nums) and k >= 0:
			k -= 1
		pq = nums[i:i+k+1]
		heapq.heapify(pq)
		nums[i] = heapq.heappop(pq)



def sort_k_sorted_num(nums, k):
	if not nums or k > len(nums):
		exit(-1)

	pq = nums[:k+1]
	heapq.heapify(pq)

	j = 0
	for i in range(k+1, len(nums)):
		nums[j] = heapq.heapreplace(pq, nums[i])
		j += 1


	while j < len(nums):
		nums[j] = heapq.heappop(pq)
		j += 1
	print(nums)


if __name__ == '__main__':
	k = 2
	arr = [4, 1, 5, 2, 3, 7, 8, 6, 10, 9]
	sort_k_sorted_num(arr, k)