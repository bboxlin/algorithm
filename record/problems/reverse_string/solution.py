class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        size = len(s)
        half = size//2
        for i in range(0, half):
            temp = s[i]
            s[i] = s[size-i-1]
            s[size-i-1] = temp
            