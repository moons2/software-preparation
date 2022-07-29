'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''


'''
A primeira abordagem que eu adotaria seria percorrer o vetor original
e inserindo os elementos do vetor original na posição referente a rotação k 

A complexidade de tempo seria O(n)
e a espacial também
'''


# First solution
def RotateVectorRight(vector, k):
	for i in range(k):
		value = vector.pop()
		vector.insert(0, value)


# Perfect Solution
def RotateVectorRight(nums, k):
	n = len(nums)
	if n == 1 or n == 0:
		return
	nums[:] = nums[:n-k%n] + nums[n-k%n:]

