class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        lmin = costs[:candidates]
        rmin = costs[max(candidates, len(costs)-candidates):]
        heapq.heapify(lmin)
        heapq.heapify(rmin)
        
        ans = 0
        l, r = candidates, len(costs)-candidates-1

        for _ in range(k):
            if lmin and rmin:
                if lmin[0] <= rmin[0]:
                    ans += heapq.heappop(lmin)
                    if l <= r:
                        heapq.heappush(lmin, costs[l])
                        l += 1
                else:
                    ans += heapq.heappop(rmin)
                    if l <= r:
                        heapq.heappush(rmin, costs[r])
                        r -= 1
            elif lmin: 
                ans += heapq.heappop(lmin)
            else: 
                ans += heapq.heappop(rmin)
                         
        return ans
        
        