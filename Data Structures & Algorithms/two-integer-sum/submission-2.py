class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevIndices = {}

        for index, value in enumerate(nums):
            difference = target - value
            if difference in prevIndices:
                return [prevIndices[difference], index]
            prevIndices[value] = index
            

        