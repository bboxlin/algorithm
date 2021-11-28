class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w_str1 = ""
        w_str2 = ""
        for w in word1:
            w_str1 += w
        
        for w in word2:
            w_str2 += w
        
        return w_str1 == w_str2