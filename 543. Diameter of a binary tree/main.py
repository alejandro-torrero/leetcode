from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:     
        # Base case for when root is none
        if root is None:
            return 0
        
        res = 0     

        def dfs(node):
            nonlocal res     
            if node is None:
                return 0
                                    
            leftDepth = dfs(node.left)
                        
            rightDepth = dfs(node.right)
            
            res = max(res,leftDepth+rightDepth)
            
            return 1 + max(leftDepth,rightDepth)   

        dfs(root)
        return res
    

node4=TreeNode(4)
node5=TreeNode(5)
node2 = TreeNode(2,node4,node5)
node3 = TreeNode(3)

root = TreeNode(1,node2,node3)    

sol = Solution()
print(sol.diameterOfBinaryTree(root))
    
    

    
    