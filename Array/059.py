'''
59. Spiral Matrix II

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:

[
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]

'''

'''
A:
brute force O(N) solution. Same recursion as the rotation problem
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        
        matrix = [  [0 for i in xrange(n)] for j in xrange(n) ]
        
        def recurse(matrix, size, shift, val):
            #left to right
            
            if size ==0:
                return matrix
            
            elif size ==1:
                matrix[shift][shift] = val
                return matrix
            
            #left to right
            for i in xrange(size):
                matrix[shift][shift+i] = val
                val +=1
                
            # top to bottom
            for i in xrange(1,size):
                matrix[shift+i][shift+size-1] = val
                val += 1
                
            # right to left
            for i in xrange(1,size):
                matrix[shift+size-1][-1-i-shift] = val
                val +=1
                
            # bottom to top
            for i in xrange(1,size-1):
                matrix[-1-i-shift][shift] = val
                val += 1
                
            return recurse(matrix, size-2, shift+1, val  )

            

    return recurse(matrix, n, 0, 1)


                                                                                                                                                                                                                                                                                                                                                                
