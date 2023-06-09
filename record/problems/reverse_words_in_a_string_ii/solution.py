class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reverse(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        
         
        reverse(0, len(s)-1 )
        
        i = 0
        while i < len(s):
            k = i
            while k < len(s) and s[k] != " ":
                k += 1
            reverse(i, k-1)
            i = k + 1
        
         
            