class Solution:
    def frequencySort(self, s: str) -> str:
        cnter = Counter(s)
        maxheap = [ (-f, c) for c,f in cnter.items() ]
        heapq.heapify(maxheap)
        ans = ""
        while maxheap:
            f,c = heapq.heappop(maxheap)
            ans += (-1)*f*c
        return ans