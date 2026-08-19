class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wordList = defaultdict(list)

        for words in strs:
            characterList = [0] * 26
            for letters in words:
                characterList[ord(letters) - ord('a')] += 1
            wordList[tuple(characterList)].append(words)
        return list(wordList.values())
            



        