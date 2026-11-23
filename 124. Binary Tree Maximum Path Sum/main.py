# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        if root is None:
            return 0        
        
        res = float('-inf')
        
        def dfs(node):
            nonlocal res

            if not node:
                return 0

            leftPath = max(0, dfs(node.left))
            rightPath = max(0, dfs(node.right))

            res = max(res, node.val + leftPath + rightPath)

            return node.val + max(leftPath, rightPath)
        dfs(root)
        
        return res                

node7 = TreeNode(7)
node15 = TreeNode(15)

node9 = TreeNode(9)
node20 = TreeNode(20,node15,node7)

root = TreeNode(-10,node9,node20)

sol = Solution()
print(sol.maxPathSum(root))