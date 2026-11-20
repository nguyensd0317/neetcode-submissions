class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)
        starts = []

        if nums == []:
            return 0

        for values in nSet:
            if values-1 not in nSet:
                starts.append(values)
        
        longest = 1
        for values in starts:
            length = 1
            i = 1
            while values+i in nSet:
                print("hi")
                i += 1
                length += 1
                longest = max(length, longest)
        
        return(longest)
                
        