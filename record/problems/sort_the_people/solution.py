class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        maxHeap = []
        for i in range(n):
            name = names[i]
            height = heights[i]
            maxHeap.append((-height,name))
        heapq.heapify(maxHeap)
        ans = []
        while maxHeap:
            h, name = heapq.heappop(maxHeap)
            ans.append(name)
        return ans