# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
        dummyHead = ListNode()
        ptr = dummyHead
        
        minHeap = []
        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(minHeap, (l.val, idx))
                lists[idx] = lists[idx].next
  
        while minHeap:
            curMinVal, curMinIdx = heapq.heappop(minHeap)
            
            ptr.next = ListNode(curMinVal)
            ptr = ptr.next 
            
            if lists[curMinIdx]:
                heapq.heappush(minHeap, (lists[curMinIdx].val, curMinIdx))
                lists[curMinIdx] = lists[curMinIdx].next

        return dummyHead.next
