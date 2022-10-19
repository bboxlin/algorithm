class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordcnt = Counter(words)
        maxheap = [ (-freq, word) for word, freq in wordcnt.items() ]
        heapq.heapify(maxheap)
        ans = []
        while k:
            ans.append(heapq.heappop(maxheap)[1])
            k -= 1
        return ans