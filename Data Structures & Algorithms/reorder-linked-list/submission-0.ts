
class Solution {
    /**
     * @param {ListNode} head
     * @return {void}
     */
    reorderList(head: ListNode | null): void {
        if (!head || !head.next) return;
        // 1. find the second half of the linked list
        let slow = head; let fast = head.next;

        while (fast && fast.next) {
            slow = slow.next;
            fast = fast.next.next;
        }
        // 2. get the second half of the linked list and detach it from the first half
        let secondHead = slow.next;
        slow.next = null

        // 3. reverse the second half
        let prev = null;
        while (secondHead) {
            let temp = secondHead.next;
            secondHead.next = prev;
            prev = secondHead;
            secondHead = temp;
        }
        secondHead = prev;

        // 3. Merge the first and the second reversed half
        let firstHead = head;

        while (secondHead) {
            let temp1 = firstHead.next;
            let temp2 = secondHead.next;

            firstHead.next = secondHead;
            secondHead.next = temp1;

            firstHead = temp1;
            secondHead = temp2;
        }
    }
}
