class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        allowSet = set(allowed)
        for word in words:
            wordSet = set(word)
            if wordSet & allowSet == wordSet:
                cnt +=1 
        return cnt