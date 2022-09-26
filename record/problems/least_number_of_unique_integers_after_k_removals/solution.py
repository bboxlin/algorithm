class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqTable = Counter(arr)
        n = len(arr)
        minheap = [ (freq, num) for num, freq in freqTable.items()]
        heapq.heapify(minheap)
 
        while minheap:
            if k - minheap[0][0] < 0:
                break 
            freq, num = heappop(minheap)
            k -= freq

        return len(minheap)
   