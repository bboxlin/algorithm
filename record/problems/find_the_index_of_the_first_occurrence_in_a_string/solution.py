class Solution:
    
    def isMatch(self, idx, haystack, needle):
        j = 0
        while idx < len(haystack) and j < len(needle) and haystack[idx] == needle[j]:
            idx += 1
            j += 1
        return j == len(needle)
    
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range( len(haystack) ):
            if haystack[i] == needle[0]:
                if self.isMatch(i, haystack, needle):
                    return i
        return -1
    