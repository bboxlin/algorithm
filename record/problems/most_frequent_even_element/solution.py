class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freqCnt = Counter(nums)
        maxHeap = [ (-freq, num) for num, freq in freqCnt.items() ]
        heapq.heapify(maxHeap)
        while maxHeap and maxHeap[0][1] % 2 != 0:
            heapq.heappop(maxHeap)
        return maxHeap[0][1] if maxHeap else -1
        