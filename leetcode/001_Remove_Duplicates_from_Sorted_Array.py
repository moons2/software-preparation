# my solution

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        r = len(nums)-1
        k = len(nums)
        
        for l in range(len(nums)-2, -1, -1):
            if nums[l] == nums[l+1]:
                for i in range(l,r):
                    nums[i]=nums[i+1]
                r -= 1
                k -= 1
        return k

# best solution

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		if len(nums) == 1:
			return 1

		i = 0
		point = None

		for r in range(len(nums)):
			if point != nums[r]:
				nums[i] = nums[r]
				point = nums[r]
				i += 1

		return i