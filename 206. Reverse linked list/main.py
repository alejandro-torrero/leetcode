# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val
        
        
        
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        reverseNode = None
        temp = None
        newHead = None
        
        if head is None:
            return None                
            
        while (head):            
            if head.next is None:
                # There's no more nodes to reverse
                newHead = head
            
            # Go through each node
            temp = head.next            
            head.next = reverseNode            
            reverseNode = head
            head = temp
            
        
        return newHead
    
n5 = ListNode(5)
n4 = ListNode(4,n5)
n3 = ListNode(3,n4)
n2 = ListNode(2,n3)
n1 = ListNode(1,n2)

sol = Solution()
print(sol.reverseList(n1))