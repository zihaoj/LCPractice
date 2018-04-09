'''
Follow up for "Unique Paths":
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
Note: m and n will be at most 100.
'''


'''
use DP, essential to realize that we rely on the bounds [x,0] and [0,y] to do induction. 
path [i][j]= path[i-1][j]+path[i][j-1]
Hence need to intialize them to be 0 if there is an obstacle behind. 
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        table = [ [1 for i in range(n)] for j in range(m) ]
        
        
        for i in range(m):
            if  obstacleGrid[i][0]==1:
                for j in range(i,m):
                    table[j][0] =0

        for i in range(n):
            if  obstacleGrid[0][i]==1:
                for j in range(i,n):
                    table[0][j] =0
                    
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] ==1:
                    table[i][j]=0
                else:
                    left = table[i-1][j]
                    up = table [i][j-1]
                    table[i][j] = left+up


        return table[m-1][n-1]
                                                                                                                                                                                                                                                                                                    
