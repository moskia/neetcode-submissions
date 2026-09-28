# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
        newLists = []
        for i in range(0, len(lists), 2):
            if i == len(lists)-1: 
                mergedList = self.merge2Lists(lists[i], None)
                newLists.append(mergedList)
            else:
                mergedList = self.merge2Lists(lists[i], lists[i+1])
                newLists.append(mergedList)
        
        return self.mergeKLists(newLists)


    def merge2Lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(None)
        tail = dummy

        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else: 
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        
        if list1: tail.next = list1
        if list2: tail.next = list2

        return dummy.next
