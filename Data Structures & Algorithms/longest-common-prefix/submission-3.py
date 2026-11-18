class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        pre = ""

        strs.sort()
        index = 0

        if len(strs) == 0:
            return ""

        while index < len(strs[0]) and index < len(strs[-1]) and strs[0][index] == strs[-1][index]:
            pre += strs[0][index]
            index += 1
        
        return pre
        