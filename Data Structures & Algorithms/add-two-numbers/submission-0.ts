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
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode {

        let dummy = new ListNode(0);
        let head = dummy;

        let rest = 0;
        while(l1 || l2 || rest) {
            let val1 = l1 ? l1.val : 0;
            let val2 = l2 ? l2.val : 0;
            let res = val1 + val2 + rest;
            rest = Math.floor(res/10);

            head.next = new ListNode(res%10);
            head = head.next;

            if (l1) l1 = l1.next;
            if (l2) l2 = l2.next;
        }

        return dummy.next;
    }
}
