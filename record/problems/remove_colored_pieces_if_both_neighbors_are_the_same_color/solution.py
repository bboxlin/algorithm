class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        acnt, bcnt = 0, 0
        l = 0
        while l < len(colors):
            r = l
            while r < len(colors) and colors[l] == colors[r]:
                r += 1
            if r - l >= 3:
                acnt += r-l-2 if colors[l] == 'A' else 0
                bcnt += r-l-2 if colors[l] == 'B' else 0        
            l = r
        return acnt > bcnt
        
        
       
                
            
                