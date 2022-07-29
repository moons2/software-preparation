class Solution:
	# mySolution
	def moveZeroes(self, nums):
		l = 0
        r = 0
        
        while l != len(nums)-1  and r != len(nums)-1:
            while nums[l] != 0 and l != len(nums)-1:
                l += 1
            if r < l:
                r = l
            while nums[r] == 0 and r != len(nums)-1:
                r += 1
            nums[l], nums[r] = nums[r], nums[l]

	# aCoolSolution
	def moveZeroes2(self, nums):
		l = 0
		for r in range(len(nums)):
			if nums[r]:
				nums[l], nums[r] = nums[r], nums[l]
				l += 1
