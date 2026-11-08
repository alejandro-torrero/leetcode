# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        # Early return
        if not root:
            return 0
        
        queue = []
        maxWidth = 0
        
        queue.append((root,0))
        
        while queue:
            levelSize = len(queue)            
            print('size', levelSize)
            _,firstIdx = queue[0]
            _, lastIdx = queue[-1]
            
            maxWidth = max(maxWidth, lastIdx-firstIdx+1)                        
            # Explore the whole level
            
            for _ in range(levelSize):
                node,idx = queue.pop(0)                            
                if node:                
                    print('Processing', node.val)     
                    if node.left:                                               
                        queue.append((node.left,2 * idx))
                    if node.right:
                        queue.append((node.right,2*idx+1))
        
        return maxWidth


# Base nodes

node5 = TreeNode(5)
node3 = TreeNode(3)
node9 = TreeNode(9)

# Second level
node3a = TreeNode(3,node5,node3)
node2a = TreeNode(2,None,node9)

head = TreeNode(1,node3a,node2a)

sol = Solution()
print(sol.widthOfBinaryTree(head))