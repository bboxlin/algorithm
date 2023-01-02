class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        uppercnt = 0
        for cha in word:
            if cha.isupper():
                uppercnt += 1
        if uppercnt == len(word):
            return True 
        elif uppercnt == 0:
            return True 
        elif uppercnt == 1 and word[0].isupper():
            return True 
        else:
            return False
             
