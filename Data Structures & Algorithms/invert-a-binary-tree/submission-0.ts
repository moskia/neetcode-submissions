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
     * @return {TreeNode}
     */
    invertTree(root: TreeNode | null): TreeNode {
        if (!root) return root;
        let queue = [root];

        while (queue.length) {
            let node = queue.shift();
                if (node.left) queue.push(node.left)
                if (node.right) queue.push(node.right)

                this.reverse(node);
        }

        return root;
    }

    reverse(root: TreeNode | null): TreeNode {
        if (!root) return root;
        let temp = root?.left ?? null;
        root.left = root?.right ?? null;
        root.right = temp;
        return root;
    }
}
