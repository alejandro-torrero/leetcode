# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        ctrArray = []
        node = head
        i = 0
        j = 0
        
        while node is not None:                 
            i = i+1
            ctrArray.append(node)
            
            if i > n:
                # Start moving second pointer                
                j = j + 1
                
            node = node.next                    
        
        if i == n:            
            # Remove the first element
            ctrArray.pop(0)
            if len(ctrArray)>0:
                newHead = ctrArray.pop(0)
                return newHead
            else:
                return None                              
        
        if j == 0:
            # Remove the last element
            ctrArray.pop()
            if len(ctrArray) > 0:
                newHead = ctrArray.pop()
                newHead.next = None
                return newHead
            else:
                return None
            
        
        if j + 2 <= len(ctrArray):
            # Next element after the remove one exists, link up
            ctrArray[j-1].next = ctrArray[j+1]
        else:
            ctrArray[j-1].next = None
            return head            
                
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
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)
node10 = ListNode(10)

node1.next = node2
node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6
# node6.next = node7
# node7.next = node8
# node8.next = node9
# node9.next = node10

    
sol = Solution()

print(sol.removeNthFromEnd(node1,3))