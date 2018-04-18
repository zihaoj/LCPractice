'''
11. Container With Most Water
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.

'''

'''
Important to realize that the two edges we pick are bounded by the smaller one
We use the two pointer case algorithm
Start with the boundary ones, this will give the largest width
Then we can remove the shorter edge and move the pointer towards the other
This is because we already know that we don't have to consider it for the current width, which is the largest it could achieve
'''



class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        
        Max = 0
        i = 0
        j = len(height)-1
        
        while i<j:
            thissize = (j-i)*min(height[i], height[j])
            if thissize >Max:
                Max = thissize
            if height[i]< height[j]:
                i+= 1
            else:
                j -=1

        return Max
                                                                                                                                                         
