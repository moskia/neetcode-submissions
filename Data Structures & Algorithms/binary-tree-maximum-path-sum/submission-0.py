# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root: Optional[TreeNode]):
            nonlocal res
            if root is None : return 0

            maxLeft = max(0, dfs(root.left))
            maxRight = max(0, dfs(root.right))

            res = max(res, root.val + maxLeft + maxRight)
            return root.val + max(maxLeft, maxRight)

        dfs(root)
        return res

