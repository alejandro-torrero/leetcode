# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        
        currentNode = head
        lastNode = None
        changeOnDifferent = False
        
        while currentNode is not None:                                                
            
            if lastNode == None:
                # Define first last node
                lastNode = currentNode
                # Advance to the next node
                currentNode = currentNode.next
                continue
                
            # Validate change
            
            if lastNode.val == currentNode.val:                
                # Found repeated alue. currentNode must advance until a different one is found
                changeOnDifferent = True
                currentNode = currentNode.next
                continue
            
            if lastNode.val != currentNode.val and not changeOnDifferent:
                # move forward on both nodes
                lastNode = currentNode                
                
            elif lastNode.val != currentNode.val and changeOnDifferent:                
                # relink nodes
                lastNode.next = currentNode
                lastNode = currentNode
                changeOnDifferent=False
                                            
            currentNode = currentNode.next  
        
        if changeOnDifferent:            
            # A change was pending
            lastNode.next = None
        
        self.printGraph(head)

        return head
    
    def printGraph(self, head):
        node = head
        while node is not None:
            print(node.val)
            node = node.next
            
            
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)
node6 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

sol = Solution()
print(sol.deleteDuplicates(node1))