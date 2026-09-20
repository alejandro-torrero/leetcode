# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        stack = []
        stack.append({"node":root,"accVal":0})
        res = False
        
        while stack:
            stackedNode = stack.pop()
            node = stackedNode["node"]
            accVal = stackedNode["accVal"]            

            print(f"Processing {stackedNode}")
            
            isLeaf = node.left == None and node.right == None            
            
            if isLeaf and accVal+node.val == targetSum:
                # Fond the tree to leaf path
                res = True
                break;       
            
            if node.left:
                stack.append({"node":node.left,"accVal":accVal+node.val})
            
            if node.right:
                stack.append({"node": node.right,"accVal":accVal+node.val})
        
        return res
    
    

# Define tree

nodeRoot = TreeNode(5)
node4 = TreeNode(4)
node8 = TreeNode(8)
node11 = TreeNode(11)
node7 = TreeNode(7)
node2 = TreeNode(2)
node13 = TreeNode(13)
node4r = TreeNode(4)
node1 = TreeNode(1)

nodeRoot.left = node4
nodeRoot.right= node8

node4.left = node11

node8.left = node13
node8.right = node4r

node11.left = node7
node11.right=node2

node4r.right = node1

sol = Solution()
print(sol.hasPathSum(nodeRoot,22))