class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        res = None
        for i in range(len(nums)):
            if res == None:
                count += 1
                res = nums[i]
            if nums[i] != res and count > 0:
                count -= 1
                if count == 0:
                    res = nums[i]
            else:
                count += 1
        
        return(res)
