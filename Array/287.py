'''
287. Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

'''


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        Two approaches if the constraints do not exist:
        (1) sort then loop, easy, space complexity is O(1) or O(n) while time complexity is O(nlogn)
        (2) use set to store visted items, space complexity is O(n) and time complexity is O(n)
        
        
        To show we must have duplicate is easy (pigeon hole)
        Since 0 is an index and 0 is not in the range, we hence must have a cycle.         
        
        use Floyd's tortoise and hare algorithm for circle detection gives O(n) run time and O(1) storage
        
        Algorithm: 
        
        Phase 1: for a sequence entering cycles from element x_m and length of cycle being l, 
        we must have for i=k*l>=m, x_i = x_2i. Therefore we just need to keep track of two pointers, one moves forward
        one step and the other moves forward two steps at a time. Once they meet we know that we are in a random point
        n on the cycle
        
        Phase 2: to find the enterting point of the cycle. We reset tortoise to point 0 and keep hare at n
        The distance between them is constantly 2l if we now move both of them at same speed. 
        By the time tortoise reachs m, hare will be at m+2l. Therefore we find the entering point. 
        
        '''
        
        
        '''
        Phase one
        
        '''
        
        h = 0
        t = 0
        
        while t==0 or t!=h:
            t = nums[t]
            h = nums[nums[h]]

        '''
        Phase two
        '''
        t = 0
        
        while t!=h:
            t =nums[t]
            h = nums[h]
            
        return t
        
        

