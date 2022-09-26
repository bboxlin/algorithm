class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        ans = ""
        if n < 1: return ans 
        randomStr = strs[0]
        for i in range( len(randomStr) ):
            for word in strs:
                if i == len(word) or word[i] != randomStr[i]:
                    return ans
            ans += randomStr[i]
        return ans
        
        