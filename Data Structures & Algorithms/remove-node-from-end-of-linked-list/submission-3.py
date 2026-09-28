# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        k = 1
        while k <= n:
            k += 1
            fast = fast.next
        
        dummy = prev = ListNode(0, head)
        while fast: 
            slow = slow.next
            fast = fast.next
            prev = prev.next
        
        prev.next = slow.next

        return dummy.next

