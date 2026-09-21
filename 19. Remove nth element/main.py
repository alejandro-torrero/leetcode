# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        stack = []
        node = head        

        # Fill stack with every node
        while node is not None:            
            stack.append(node)
            node = node.next
            
        print(stack)

        # Backtrack n element

        i = 1
        lastNode = None
        while i <= n:
            lastNode = stack.pop()
            i =i+1
        
        if len(stack) == 0:
            return None
        
        toConect = stack.pop()                
        
        toConect.next = lastNode.next
        
        self.printGraph(head)

        return head
    
    def printGraph(self,node:ListNode):
        while node is not None:
            print(f"Node {node.val}")
            node = node.next
    
    
    
# Create nodes

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
    
sol = Solution()

print(sol.removeNthFromEnd(node1,2))