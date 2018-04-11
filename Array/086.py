'''
86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''


'''
Purely manipulation of linked list. 

Initialize a header and a moving list for both left and right sets with dummy node
while the moving list moves forward, the header stays at the original 
value and can be used to link two sets together

left.next = h2.next # links two sets
return h1.next get rid off the starting dummy node


'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        left  = h1= ListNode(0)
        right = h2 = ListNode(0)
        
        while head:
            if head.val<x:
                left.next  = head
                left = left.next
            else:
                right.next = head
                right = right.next
                head = head.next
                
                right.next = None
                left.next = h2.next

        return h1.next
                                                                                                                                        
