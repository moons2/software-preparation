




# my solution
class Solution:
    def containsDuplicate(self, nums):
        if len(nums) < 2
            False
        mySet = set()
        for _, v in enumerate(nums):
            if v in mySet:
                return True
            mySet.add(v)


# prettier solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(nums) == len(set_nums): return False
        else: return True