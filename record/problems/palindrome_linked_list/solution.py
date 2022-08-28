# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def check(node, stk):
            while node and stk[-1] == node.val:
                node = node.next 
                stk.pop()
            return len(stk) == 0 and node == None
                
        stack = [] 
        slow, fast = head, head 
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next 
            
        if len(stack) == 0:return True
        return check(slow, stack[:]) or check(slow.next, stack[:])
        
        
            