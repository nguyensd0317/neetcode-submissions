class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Look through every word and see if there exists the same character

        prefix = ""
        if len(strs) == 0:
            return prefix
        if len(strs) == 1:
            return strs[0]
        flag = False
        for i in range(len(strs[0])):
            flag = False
            for j in range(1, len(strs)):
                if i < len(strs[j]) and strs[j][i] == strs[0][i]:
                    flag = True
                else:
                    return prefix
            if flag:
                prefix += strs[0][i] 
        
        return prefix