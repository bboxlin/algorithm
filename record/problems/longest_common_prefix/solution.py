class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = float('inf')
        for s in strs:
            length = min(length, len(s))
            
        j = 0
        flag = False
        for _ in range(length): 
            for i in range(1, len(strs)):
                if strs[i][j] != strs[i-1][j]:
                    return strs[0][:j]
                    break
            j += 1            
 
        return strs[0][:j]
            
                
            