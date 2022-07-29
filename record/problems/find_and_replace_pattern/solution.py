class Solution:
    
    def isMatch(self, wordx, wordy):
        if len(wordx) != len(wordy):
            return False
        x2y, y2x = {}, {}
        for i in range(len(wordx)):
            x = wordx[i]
            y = wordy[i]
            if x not in x2y.keys():
                x2y[x] = y
            if y not in y2x.keys():
                y2x[y] = x
            if x2y[x] != y or y2x[y] != x:
                return False
        return True
        
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for w in words:
            if self.isMatch(w, pattern):
                ans.append(w)
        return ans
     
                        
            
            
        