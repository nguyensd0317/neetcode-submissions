class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Characters = {}
        SChar = defaultdict(int)
        TChar = defaultdict(int)
        for letters in s:
            SChar[letters] += 1
        for letters in t:
            TChar[letters] += 1
        
        if TChar != SChar:
            return False
        
        return True

        