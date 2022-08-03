# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1, stk2 = [], []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next 
        while l2:
            stk2.append(l2.val)
            l2 = l2.next 

        prev = None
        carry = 0 
        while stk1 or stk2 or carry:
            if stk1:
                carry += stk1.pop()
            if stk2:
                carry += stk2.pop()
            curnode = ListNode(carry%10)
            curnode.next = prev 
            prev = curnode
            carry = carry // 10
        return prev
            
            