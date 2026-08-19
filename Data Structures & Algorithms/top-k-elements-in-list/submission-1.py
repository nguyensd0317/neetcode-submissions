from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        listOfOccurences = []
        for i in range(len(nums)):
            listOfOccurences.append([])
        
        countedNumbers = Counter(nums)

        for value, count in countedNumbers.items():
            listOfOccurences[count-1].append(value)
        
        answer = []
        for countBackwards in range(len(nums)-1, -1, -1):
            for valuesInList in listOfOccurences[countBackwards]:
                answer.append(valuesInList)
                if len(answer) == k:
                    return answer


            


        
        
        
        