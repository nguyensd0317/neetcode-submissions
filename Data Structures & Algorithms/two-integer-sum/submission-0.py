class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashBrown = {}

        for index, value in enumerate(nums):
            hashBrown[value] = index
        
        for i in range(len(nums)):
            compliment = target-nums[i]
            if (compliment in hashBrown.keys() and hashBrown[compliment] != i):
                return [i, hashBrown[compliment]]
        return []
        