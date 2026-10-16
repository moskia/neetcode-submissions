"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copy = Node(head.val)
        dummy1 = copy
        dummy2 = head
        identifier = {}

        # First pass: copy nodes and build the mapping
        while dummy2:
            identifier[dummy2] = dummy1

            if not dummy2.next:
                break

            dummy2 = dummy2.next
            dummy1.next = Node(dummy2.val)
            dummy1 = dummy1.next

        # Second pass: assign random pointers
        rdummy2 = head
        rdummy1 = copy

        while rdummy2:
            rdummy1.random = identifier.get(rdummy2.random)
            rdummy1 = rdummy1.next
            rdummy2 = rdummy2.next

        return copy