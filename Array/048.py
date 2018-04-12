'''
048.Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

'''


'''
key to realize
x1, y1 = 0, i
x2, y2 = i, size-1
x3, y3 = size-x1-1, size-y1-1
x4, y4 = size-x2-1, size-y2-1
'''


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        s = 0
        
        
        def recurse( matrix  , size, s):
            if size <2:
                return matrix
            else:
                for i in range(size-1):
                    x1, y1 = 0, i
                    x2, y2 = i, size-1
                    x3, y3 = size-x1-1, size-y1-1
                    x4, y4 = size-x2-1, size-y2-1
                    
                    a1 = matrix[x1+s][y1+s]
                    a2 = matrix[x2+s][y2+s]
                    a3 = matrix[x3+s][y3+s]
                    a4 = matrix[x4+s][y4+s]
                    
                    matrix[x4+s][y4+s] = a3
                    matrix[x1+s][y1+s] = a4
                    matrix[x2+s][y2+s] = a1
                    matrix[x3+s][y3+s] = a2
                    
            return recurse(matrix, size-2, s+1)
        
        recurse(matrix, n, s)                
