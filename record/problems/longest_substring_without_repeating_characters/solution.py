class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        max_len = 0
        i, j = 0, 0
        
        for j in range(len(s)):
            while s[j] in visited:
                visited.remove(s[i])
                i += 1
            visited.add(s[j])
            max_len = max(max_len, j-i+1)             
        return max_len
             

        
            