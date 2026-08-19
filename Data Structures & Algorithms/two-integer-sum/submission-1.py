class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashBrown = {}
        for index, value in enumerate(nums):
            hashBrown[value] = index
        
        for index in range(len(nums)):
            compliment = target - nums[index]
            if compliment in hashBrown and hashBrown[compliment] != index:
                return [index, hashBrown[compliment]]
        