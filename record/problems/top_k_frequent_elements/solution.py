import heapq

class Node:
    def __init__(self, val, frequency):
        self.val = val
        self.frequency = frequency
    
    def __lt__(self, other):
        if self.frequency > other.frequency:  
            return True    
        else:  
            return False                      

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        maxheap = [Node(val, f) for val, f in freq.items()]
        heapq.heapify(maxheap)
        ans = []
        while k:
            node = heapq.heappop(maxheap)
            ans.append(node.val)
            k -= 1
        return ans



            