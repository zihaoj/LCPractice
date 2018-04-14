'''
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''


'''
Same as the sprial matrix II problem. 
Loop over to peel off layers. 
Make sure do the right thing when encounter m ==1, n==1 cases 
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if matrix == []:
            return []
        
        m = len(matrix)
        n = len(matrix[0])

        output = []

        def recurse(matrix, m, n, output, shift):

            if m ==0 or n ==0:
                return output

            if m ==1:
                for i in xrange(n):
                    output.append(  matrix[shift][shift+i]   )
                return output
                                                                                                                                                            
            if n ==1:
                for i in xrange(m):
                    output.append(  matrix[shift+i][shift]   )

                return output

            ## left to right
            for i in xrange(n):
                output.append( matrix[shift][shift+i]  )
            
            ## top to bottom
            for i in xrange(1,m):
                #print shift+i, shift+n, shift
                output.append( matrix[shift+i][shift+n-1]   )
                
            ## right to left
            for i in xrange(1,n):
                output.append( matrix[shift+m-1][-1-i-shift])
                ## bottom to top
            for i in xrange(1, m-1):
                output.append( matrix[-1-i-shift][shift]  )
                
            return recurse(matrix, m-2, n-2, output, shift+1  )

        return recurse(matrix, m, n, output, 0)









                                                                                                                                                                                                                                                                                                                                                                                                                                                        
