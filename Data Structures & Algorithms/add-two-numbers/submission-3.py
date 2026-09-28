# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(None)
        tail = dummy
        rest = 0

        while l1 or l2:

            if l1: 
                num1 = l1.val 
                l1 = l1.next
            else: 
                num1 = 0

            if l2: 
                num2 = l2.val
                l2 = l2.next
            else: 
                num2 = 0

            sum = num1 + num2 + rest

            rest = sum//10
            val = sum%10

            tail.next = ListNode(val, None)
            tail = tail.next
        
        if rest != 0: tail.next = ListNode(rest, None)

        return dummy.next




        