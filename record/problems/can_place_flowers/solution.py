class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        length, count = len(flowerbed), 0
        
        for i in range(length):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1]==0) and (i == length-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count+=1
        return count>= n
        
                    
                
            
            
                