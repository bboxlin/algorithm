class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        size = len(arr)
        halfSize = size // 2
        maxheap = [ (-freq, val) for val, freq in Counter(arr).items() ]
        heapq.heapify(maxheap)
        ans = 0
        while  size > halfSize:
            freq, val = heapq.heappop(maxheap)
            size += freq
            ans += 1
        return ans
        
        