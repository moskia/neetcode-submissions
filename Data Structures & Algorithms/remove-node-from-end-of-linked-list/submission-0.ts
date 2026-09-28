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
        let revHead = this.reverse(head);

        let newHead = this.deleteK(revHead, n);

        return this.reverse(newHead);
    }

    deleteK(head, k) {

    // If list is empty or k is 0, return the head
    if (head === null || k <= 0) {
        return head;
    }

    let curr = head;
    let prev = null;
    let count = 0;

    // Traverse the linked list
    while (curr !== null) {
        count++;

        // If count is a multiple of k, remove 
        // current node
        if (count === k) {
        
            // skip the current node
            if (prev !== null) {
                prev.next = curr.next;
            } 
            else {
            
                // If removing the head node
                head = curr.next;
            }
        } 
        else {
        
            // Update previous node pointer only if
            // we do not remove the node
            prev = curr;
        }
        curr = curr.next;
    }
    return head;
    }

    reverse(head: ListNode | null): ListNode {
        let prev = null;
        while (head) {
            let temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }

        return prev;
    }
}
