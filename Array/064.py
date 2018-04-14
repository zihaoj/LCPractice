'''
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
  [4,2,1]]

Given the above grid map, return 7. 
'''

'''
Use DP, keep table of the min up to [i,j]
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if grid == []:
            return 0
        
        m = len(grid)
        n = len(grid[0])

        table = [ [0 for i in xrange(n)] for j in xrange(m) ]

        table[0][0] = grid[0][0]

        for j in xrange(1, n):
            table[0][j] = table[0][j-1]+grid[0][j]
            
        for i in xrange(1, m):
            table[i][0] = table[i-1][0]+grid[i][0]
            
        for i in xrange(1, m):
            for j in xrange(1, n):
                table[i][j] = min( table[i-1][j], table[i][j-1]) +  grid[i][j]

        return table[-1][-1]
