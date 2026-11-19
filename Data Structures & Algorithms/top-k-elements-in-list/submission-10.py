class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bucket = [[] for _ in range(len(nums) + 1)]

        count = Counter(nums)
        
        for number, nCount in count.items():
            bucket[nCount].append(number)

        final = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i] == []:
                continue
            for j in range(len(bucket[i]) - 1, -1, -1):
                if k == 0:
                    return final
                else:
                    final.append(bucket[i][j])
                    k -= 1

        return final