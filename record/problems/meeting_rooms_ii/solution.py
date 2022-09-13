import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        rooms = 1
        sorted_interval = sorted(intervals)
        min_heap = [sorted_interval[0][1]]
        for start, end in sorted_interval[1:]:
            last_end = min_heap[0]
            if start < last_end:
                rooms += 1
                heapq.heappush(min_heap, end)
            else:
                # merge the meeting
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, end)
            
        print(len(min_heap))
        return rooms
    
        # [[4,9],[4,17],[9,10]]
        #          2 