# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        queue = deque([root, None])
        rightSide = [root.val]

        while queue:
            node = queue.popleft()

            if node is None:
                if queue: 
                    rightSide.append(queue[0].val)
                    queue.append(None)
                continue

            if node.right:
                queue.append(node.right)

            if node.left:
                queue.append(node.left)

        return rightSide
