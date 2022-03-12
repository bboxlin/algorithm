import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap=[]
        j=0
        n=len(events)
        res=0
        # 枚举每一时刻
        for day in range(1,100001):
            # 删掉过期会议
            while heap and heap[0]<day:
                heappop(heap)
            # 加入可选会议
            while j<n and events[j][0]==day:
                heappush(heap,events[j][1])
                j+=1
            # 参加最先结束的会议
            if heap:
                heappop(heap)
                res+=1
            if j > n: break
        return res
 