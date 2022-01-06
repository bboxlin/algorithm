class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_used = [] #min heap
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff <= 0: continue
            heapq.heappush(ladder_used, diff)
            # by far the smallest diff give to bricks
            if len(ladder_used) > ladders:
                bricks -= heapq.heappop(ladder_used)
            if bricks < 0:
                return i-1
        return len(heights) - 1
            
             
        
        
            