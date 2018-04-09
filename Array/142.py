'''
142. Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?


'''

'''
tortoise and hare again
note that we can nest the two while.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        '''
        use tortoise and hare
        '''
        
        h = head
        t = head
        
        if head == None:
            return None
                                                    
        while ( h and h.next):
            h = (h.next).next
            t = t.next
            
            if h ==t:
                '''
                phase 2
                '''
                t = head
                while (h != t):
                    h = h.next
                    t = t.next
                    return h
                
        return None
