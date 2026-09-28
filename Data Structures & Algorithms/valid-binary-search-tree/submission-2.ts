/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isValidBST(root: TreeNode | null): boolean {
        if (!root) return true;
        return this.isValid(root, -Infinity, Infinity)
    }

    isValid(root: TreeNode | null, left: number, right: number): boolean {
        if (!root) return true;
        if (root.val > left && root.val < right) {
            return this.isValid(root.left, left, root.val) && this.isValid(root.right, root.val, right);
        }
        return false;
    }
}
