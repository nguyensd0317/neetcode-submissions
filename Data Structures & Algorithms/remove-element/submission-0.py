class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # If I see an element that is equal to the value, I'll just not do anything
        # otherwise I think we just write the value down then, everytime we write
        # it down we keep track

        # 3, 2, 2, 3

        # i = 1
        # 2
        # write = 0
        
        # 2 -> nums[write]
        # write += 1
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
            