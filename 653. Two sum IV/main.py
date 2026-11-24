from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lookup = set()
        stack =[]

        while root:
            if (k-root.val) in lookup:
                return True

            lookup.add(root.val)

            if root.left:
                stack.append(root.left)

            if root.right:
                stack.append(root.right)
            
            if len(stack)> 0:
                root = stack.pop(0)
            else:
                root = None
        return False