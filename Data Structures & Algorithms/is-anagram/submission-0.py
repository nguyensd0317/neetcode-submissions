class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap = {}
        hashMap2 = {}
        for values in s:
            if values in hashMap:
                hashMap[values] += 1
            else:
                hashMap[values] = 1

        for values in t:
            if values in hashMap2:
                hashMap2[values] += 1
            else:
                hashMap2[values] = 1

        return (hashMap == hashMap2)
                
            

        