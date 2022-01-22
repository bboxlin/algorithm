import heapq
class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     freq = {}
    #     for n in nums:
    #         if n not in freq:
    #             freq[n] = 1
    #         else:
    #             freq[n] += 1
    #     max_heap = [(-fre, n) for n, fre in freq.items()]
    #     heapq.heapify(max_heap)
    #     res = [heapq.heappop(max_heap)[1] for i in range(k)]
    #     return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # N array slots
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # track down the frequency of each number
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        # each slot with a list container, a number appends to corresponding frequency slot
        for number, frequency in freq.items():
            buckets[frequency].append(number)
        
        # O(k) in time here 
        res = []
        N = len(buckets) - 1 
        for i in range(N, -1, -1):
            if len(buckets[i]) > 0:
                for val in buckets[i]:
                    if len(res) >= k:
                        return res
                    res.append(val)
 
        return res 
            
            

            