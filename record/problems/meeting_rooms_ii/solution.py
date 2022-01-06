import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        rooms = 1
        # make sure the interval are sorted in this way.
        sorted_interval = sorted(sorted(intervals, key = lambda x:x[1]))
        
        min_heap = [sorted_interval[0][1]]
        
        for start, end in sorted_interval[1:]:
            last_end = min_heap[0]
            if start < last_end:
                rooms += 1
            else:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
        return rooms
    
        # [[4,9],[4,17],[9,10]]
        #          2 