/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode[]} lists
     * @return {ListNode}
     */
    mergeKLists(lists: ListNode[]): ListNode {
        if (lists.length <= 1) return lists[0] ?? null;
        let result: ListNode[] = [];
        for (let i = 0; i<lists.length; i = i+2) {
            if (i === lists.length-1) {
                result.push(this.merge2Lists(lists[i], null));
            } else {
                result.push(this.merge2Lists(lists[i], lists[i+1]));
            }
        }
        return this.mergeKLists(result)
    }

    merge2Lists(l1: ListNode | null, l2: ListNode | null): ListNode {
        let dummy: ListNode | null = new ListNode(0, null);
        let head = dummy;

        while (l1 && l2) {
            if (l1.val > l2.val) {
                head.next = l2;
                l2 = l2.next
            } else {
                head.next = l1;
                l1 = l1.next
            }
            head = head.next;
        }
        head.next = l1 ?? l2;
        return dummy.next;
    }
}
