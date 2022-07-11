class Solution:
    def reorganizeString(self, S: str) -> str:
#         ans = ""
#         max_heap = [ (-freq, c) for c, freq in Counter(s).items()]
#         heapq.heapify(max_heap)
        
#         prevtup = (0, '') 
#         while max_heap:
#             maxfreq, maxc = heapq.heappop(max_heap)
#             ans += maxc 
#             maxfreq += 1
#             # push back the prevtup
#             if prevtup[0] != 0:
#                 heapq.heappush(max_heap, prevtup) 
#             prevtup = (maxfreq, maxc)    
  
#         if len(ans) != len(s): return ""
#         return ans
        if len(S) == 1:
            return S
        count = collections.Counter(S)
        digit0 = max(count.keys(), key = lambda x: count[x])
         
        an = [digit0 for _ in range(count[digit0])]
         
        
        i = 0
        for digit in count:
            if digit != digit0:
                for _ in range(count[digit]):
                    an[i%len(an)] += digit
                    i += 1
        print(an)
        print(i)
        return ''.join(an) if i >= len(an) - 1 else ''
            