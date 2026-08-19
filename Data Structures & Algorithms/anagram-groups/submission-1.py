class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wordCounter = defaultdict(list)

        for words in strs:
            singleWord = [0] * 26
            for letters in words:
                singleWord[ord(letters) - ord('a')] += 1
            wordCounter[tuple(singleWord)].append(words)
        
        return list(wordCounter.values())