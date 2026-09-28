# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        secondHalf = slow.next
        slow.next = None
        prev = None

        while secondHalf: 
            temp = secondHalf.next
            secondHalf.next, prev = prev, secondHalf
            secondHalf = temp
        
        firstHalf = head
        secondHalf = prev

        while secondHalf:
            firstNext = firstHalf.next
            secondNext = secondHalf.next

            firstHalf.next = secondHalf
            secondHalf.next = firstNext
            
            firstHalf = firstNext
            secondHalf = secondNext


