# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
[Weekly Contest 321]
[Q3]

"""
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        def dfs(prevnode, node):
            if not node:
                return -math.inf
            nxtmax = dfs(prevnode.next, node.next)
            if node.val < nxtmax:
                prevnode.next = node.next 
            return max(node.val, nxtmax)
 
        dummy = ListNode(next=head)
        dfs(dummy, head)
        return dummy.next
        
     
        
         
            
            
                
            