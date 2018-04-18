'''
73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
'''

'''

Note that these are integers marking them with -1 is not good.
Instead mark the ones going to be flipped as a character or something else then we can solve in place

Another solution from online is to use the first column and first row as storage space
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        
        '''
        shall be able to solve it in place, just mark elements as -1 if necessary
        '''
        
        if matrix ==[[]]:
            return matrix
        
        m = len(matrix)
        n = len(matrix[0])
        
        
        ### look at rows
        for i in xrange( m ):
            for j in xrange(n):
                if matrix[i][j] ==0:
                    for k in xrange(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = "a"
                            
                                                                                                                                                                                                                            break

                                                                                                                                                                                                                    ### look at cols
                                                                                                                                                                                                                    for j in xrange( n ):
            for i in xrange( m ):
                if matrix[i][j] ==0:
                    for k in xrange(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = "a"
                break
        ### make zeros
        for i in xrange( m ):
            for j in xrange(n):
                if matrix[i][j] =="a":
                    matrix[i][j] = 0

                                                                                                                                                                                                                                                                                                                                                                                                                                                                            


