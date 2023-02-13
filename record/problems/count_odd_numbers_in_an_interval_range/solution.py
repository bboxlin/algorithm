class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # 7 - 3 = 4 
        # 4 // 2 = 2 + 1 = 3

        # 10 - 8 = 2
        # 2 // 2 = 1 
        
        d = high - low 
        if high % 2 != 0 or low % 2 != 0:
            return d//2 + 1
        return d//2