# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        [1,2,3,4] n = 2
            -2 -1
        
        how long is my linked list
        1
        [0,1,3]

        find the count of my linked list
        I want to iterate through it, until it reaches that point
        I want to remove the node 

        In order to remove the node, I'm gonna use the linked list pointer prior to it
        and I'm gonna use garbage collection to remove it

        pointer 1
        pointer.next = pointer.next.next
        '''

        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        
        if n > count:
            return head
        iterator = count - n

        dummyNode = ListNode()

        dummyNode.next = head
        newHead = dummyNode

        while iterator != 0:
            dummyNode = dummyNode.next
            iterator -= 1
        dummyNode.next = dummyNode.next.next

        return newHead.next
        '''
        [*, 1, 2, 3 ,4] n = 2
        count = 4
        iterator = 2
        [*, 5]
        iterator = 0 (1 - 1)


        '''