# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        
        # Base case, graph is missing
        if head is None:
            return None
        
        stack = []        
        node = head
        i = 1
        
        while node is not None:
            stack.append(node)
            currentNode = node
            node = node.next            
            
            if i % 2 == 0:                
                # Execute swap                
                                
                # Last node swap
                lastNode = stack[i-2]
                lastNode.next = currentNode.next                                
                
                # New node
                currentNode.next = lastNode                
                
                
                # Check for precursor node                
                if i - 4 >=0 and i-4 < len(stack):
                    precursorNode = stack[i-4]                    
                    precursorNode.next = currentNode                    
                    
                if i == 2:
                    head = currentNode      
                   
            i = i + 1
                    
        return head            
        
        
    def printGraph(self, node: ListNode):
        
        while node is not None:
            print(node.val)
            node = node.next
        
    

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
    
sol = Solution()
print(sol.swapPairs(node1))