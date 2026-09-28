# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        prevGroup = dummy

        while prevGroup.next:
            curr = prevGroup.next
            prev = None
            count = 0

            # Reverse up to k nodes in a single pass
            while curr and count < k:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                count += 1

            # If we successfully reversed a full k-group
            if count == k:
                # prevGroup.next was the head of this group; now it's the tail
                tail = prevGroup.next
                tail.next = curr
                prevGroup.next = prev
                prevGroup = tail
            else:
                # Re-reverse the leftover nodes (< k) back to their original order
                curr = prev
                prev = None
                while curr:
                    tmp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = tmp
                break

        return dummy.next