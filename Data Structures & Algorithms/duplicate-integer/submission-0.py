class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for value in nums:
            if value in duplicates:
                return True
            duplicates.add(value)
            
        return False
         