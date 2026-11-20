class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        listLength = len(nums)
        final = [1] * listLength

        prefix = 1
        for i in range(listLength):
            final[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(listLength-1,-1,-1):
            final[i] *= postfix
            postfix *= nums[i]
        
        return(final)
