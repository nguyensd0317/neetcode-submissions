class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writtenNumber = 0
        for index in range(len(nums)):
            if nums[index] == val:
                continue
            nums[writtenNumber] = nums[index]
            writtenNumber += 1
        
        for index in range(writtenNumber, len(nums)):
            nums[index] = None

        print(nums, writtenNumber)
        return writtenNumber
            