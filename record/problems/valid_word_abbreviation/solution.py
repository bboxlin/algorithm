class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        counter = ""
        while i < len(word) and j < len(abbr): 
            if abbr[j].isdigit():
                counter = counter + abbr[j]
                if counter == "0": return False
                j += 1
            else:
                if len(counter) > 0: 
                    i += int(counter)
                    counter = ""  
                if i >= len(word): return False
                elif word[i] != abbr[j]:
                    return False  
                i += 1 
                j += 1
        
        # handle the case abbr end with digits
        if len(counter) > 0: 
            i += int(counter)
            
        return j == len(abbr) and i == len(word)    
