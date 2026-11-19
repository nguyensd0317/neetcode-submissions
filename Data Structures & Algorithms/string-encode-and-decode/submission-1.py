class Solution:

    def encode(self, strs: List[str]) -> str:
        eString = ""
        for values in strs:
            eString += f"{len(values)}#{values}"
        return eString
        

    def decode(self, s: str) -> List[str]:
        eList = []
        i = 0
        print(s)
        while i < len(s):
            charCount = ""
            while s[i].isdigit():
                charCount += str(s[i])
                i += 1
            if s[i] == "#" and len(charCount) > 0:
                print(i)
                charCount = int(charCount)
                start = i+1
                end = start+charCount
                eList.append(s[start:end])
                i += charCount
            i += 1
        return(eList)

