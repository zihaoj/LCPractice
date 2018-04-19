'''
120. Triangle
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
 

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''


'''
We can solve in-place with DP. So O(MN) time and O(1) space
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        
        '''
        Solve it in-place is the best I guess?
        '''
        
        if triangle == []:
            return 0
        
        m = len(triangle)
        
        
        ### use triangle to store the path

        for i in xrange( 1, m ):
            n = len(triangle[i])
            
            for j in xrange(n):
                #print i, j, max(0, j-1), min(j, n-2)
                upper_min = min(  triangle[i-1][max(0, j-1)], triangle[i-1][min(j, n-2)] )
                triangle[i][j] += upper_min
                
        return min(triangle[-1])
