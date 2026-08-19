class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        bucket = [ [] for _ in range(len(nums))]

        for values in set(nums):
            bucket[nums.count(values) - 1].append(values)
        
        final = []
        for i in range(len(bucket)-1, -1, -1):
            for numbers in bucket[i]:
                final.append(numbers)
                if len(final) == k:
                    return final