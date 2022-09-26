class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 0-30  ---> 1个房间
        # 5-10  ---> 多创建1个
        # 15-20 ---> 用5-10的房间
        intervals.sort() 
        room = 0
        minheap = []   #存放meeting结束的时间
        for begin, end in intervals:
            if not minheap or minheap[0] > begin: #如果之前最早结束的时间 > 我们当前开始的时间
                room += 1
                heappush(minheap, end)
            else:
                #如果之前最早结束的时间 <= 我们当前开始的时间 
                heappop(minheap)
                heappush(minheap, end)
        return len(minheap)
        