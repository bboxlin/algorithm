# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def divide(head):
            if not head or not head.next: 
                return head
            
            ####################### Get Med Node ##############
            slow = fast = head
            while fast.next != None and fast.next.next != None:
                fast = fast.next.next
                slow = slow.next
            ###################################################
            
            # med point next half
            med = slow.next
            # first half point None
            slow.next = None

            left = divide(head)
            right = divide(med)
            return merge(left,right)
        
        def merge(l1, l2):
            dummy = res = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            if l1: dummy.next = l1
            if l2: dummy.next = l2
            return res.next
            

                          
        return divide(head)
                    
            
            