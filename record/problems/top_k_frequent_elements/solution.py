class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time: O(nlogn)
        # Space: O(n)
#         freqDict = defaultdict(int)
#         for num in nums:
#             freqDict[num] += 1
        
#         ans = []
        
#         lst = list(freqDict.items())
#         lst.sort(key = lambda x: x[1], reverse=True)
#         return [ num for num, freq in lst[:k] ] 
    
        freqDict = defaultdict(int)
        for num in nums:
            freqDict[num] += 1
        
        ans = []
        maxheap = [ (-freq, num) for num, freq in freqDict.items() ]
        heapq.heapify(maxheap)  # o(n)
        
        while heapq and k > 0:
            nfreq, curnum = heapq.heappop(maxheap)
            ans.append(curnum)
            k -= 1
        return ans