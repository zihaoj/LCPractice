'''
718. Maximum Length of Repeated Subarray
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
'''



'''
use DP in this case        
Basically uses a table to keep track of the 
longest common suffixes up to [i,j]
similar to the unique path problem
'''



class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        

        m = len(A)
        n = len(B)
        
        table = [ [ 0 for i in xrange(n)] for j in xrange(m) ]
        
        for i in xrange(m):
            table[i][0] = (A[i] == B[0] )
            for j in xrange(n):
                table[0][j] = (A[0] == B[j] )
                
                Max = 0
                
                for i in xrange(1, m):
                    for j in xrange(1, n):
                        if A[i] ==B[j]:
                            table[i][j] = table[i-1][j-1] +1
                            Max = max( table[i][j], Max  )
                        else:
                            table[i][j] = 0
                            
        return Max


                                                                                                                                                                                                            
