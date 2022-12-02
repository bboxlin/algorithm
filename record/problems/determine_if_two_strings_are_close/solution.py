class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        cnter1 = Counter(word1)
        cnter2 = Counter(word2)
        if cnter1.keys() != cnter2.keys():
            return False 
        if sorted(cnter1.values()) != sorted(cnter2.values()):
            return False 
        return True
        