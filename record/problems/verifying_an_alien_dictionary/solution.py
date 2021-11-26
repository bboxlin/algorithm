class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def isGreater(second, first):
            i, j = 0, 0
            while i < len(first) and j < len(second):
                if memo[first[i]] > memo[second[j]]:
                    return False
                elif memo[first[i]] < memo[second[j]]:
                    return True
                i += 1
                j += 1
            
            # 1. i have some char left for traversal
            if i < len(first): return False
            
            # 2. j some some char left for traversal 
            elif j < len(second): return True
            
            # 3. in case both first and second equal all characters
            return True
       
        if len(words) == 1: return True
        memo = {}
        for index, c in enumerate(order):
            memo[c] = index
        
        for i in range(1, len(words)): # N for total N words in List
            second = words[i]
            first = words[i-1]
            if isGreater(second, first):  # M character in a sublist       #Time: O(NM)
                continue
            else:
                return False  
        return True