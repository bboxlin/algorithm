class Solution:
#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         # Time: O(n)
#         # Space: O(n)
#         # Greedy solution
#         # X = b-a, for x in X, if x is big indicating b is significantly large than a we should pick a at that position,
#         # else b is significantly smaller than a we should pick b at that position
        
#         # [ [1,3], [5,6]]
#         # diff = [2, 1]
#         n = len(costs)
#         BminusAdiff = [ (b-a, a, b)  for a, b in costs]
#         heapq.heapify(BminusAdiff) 
#         i = 0
#         ans = 0
#         while BminusAdiff:
#             diff, acost, bcost = heapq.heappop(BminusAdiff)
#             if i < n//2:
#                 ans += bcost
#             else:
#                 ans += acost
#             i += 1
#         return ans
    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        @lru_cache
        def dp(aPeople, bPeople):
            i = aPeople + bPeople
            if i == len(costs):
                return 0 if aPeople == bPeople else math.inf
            return min(dp(aPeople+1, bPeople) + costs[i][0], dp(aPeople, bPeople + 1) + costs[i][1])
        return dp(0, 0)
        
#         @cache
#         def dp(apos, bpos):
#             if apos == len(costs) or bpos == len(costs):
#                 return 0  
#             Bfirst = dp(apos+1, bpos) + costs[apos][0] + costs[bpos][1]
#             print(Bfirst)
#             Afirst = dp(apos, bpos+1) + costs[apos][0] + costs[bpos][1]
#             return min(Bfirst, Afirst)
            
#         return dp(0,0)
            
            
        