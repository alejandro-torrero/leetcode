# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        toReverse = []
        lastNode = None
        newHead = head
    
        while head:
            print(f'Processing {head.val}')            
            
            if len(toReverse) < k:
                toReverse.append(head)
            else:
                # ToReverse array is full, start reverse process 
                print(f'To reverse array full. Execute reversion')
                
                # Link lastNode to first reversed value
                if lastNode is not None:
                    lastNode.next = toReverse[-1]
                else:
                    # lastNode is none, this is the first reversion
                    newHead = toReverse[-1]
                    
                # Define next lastNode                
                
                lastReverse = None
                for i in range(k):
                    # Go through the array in reverse order
                    node = toReverse[i]
                    
                    if i == 0:
                        # Last node to reverse
                        node.next = head
                        lastReverse = node
                        lastNode = node                        
                    else:
                        node.next = lastReverse
                        lastReverse = node
                        
                # Reverse finished. Restart values                                                                            
                toReverse = [head]                
                
            head = head.next      
        
        if len(toReverse) == k:
            # Left out nodes that need reverse
            
            # Link lastNode to first reversed value
            if lastNode is not None:
                lastNode.next = toReverse[-1]
            else:
                # lastNode is none, this is the first reversion
                newHead = toReverse[-1]
            
            lastReverse = None
            for i in range(k):
                # Go through the array in reverse order
                node = toReverse[i]
                
                if i == 0:
                    # Last node to reverse
                    node.next = head
                    lastReverse = node
                    lastNode = node                        
                else:
                    node.next = lastReverse
                    lastReverse = node
            
        return newHead
    

values = [1,2]
lastNode = None

for i in range(len(values)-1,-1,-1):    
    if lastNode is None:
        lastNode = ListNode(values[i],None)
    else:
        newNode = ListNode(values[i],lastNode)
        lastNode = newNode    

sol = Solution()
newHead = sol.reverseKGroup(lastNode,2)

print("Results:")
while newHead:
    print(newHead.val)
    newHead = newHead.next