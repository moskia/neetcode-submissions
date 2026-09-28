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
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head: ListNode | null, n: number): ListNode {
        let slow = head;
        let fast = head;
        let counter = 0;
        while (counter < n) {
            fast = fast.next;
            counter++;
        }

        if (!fast) {
            return head.next;
        }

        let prev = null;
        while (fast) {
            fast = fast.next;
            prev = slow;
            slow = slow.next;
        }

        prev.next = slow.next;
        return head;
    }
}
