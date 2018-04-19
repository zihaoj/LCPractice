'''
74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

'''

'''
use binary search and modulo to find the indicies        
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if matrix == []:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        if n ==0:
            return False
        mn = m*n
        
        
        def binarySearch(start, end):
            
            mid = (start+end)/2
            
            start_i = start //  n
            start_j = start % n
            mid_i   = mid  //   n
            mid_j   = mid  %  n
            end_i   = end  //   n
            end_j   = end  %  n

            start_val = matrix[start_i][start_j]
            mid_val = matrix[mid_i][mid_j]
            end_val = matrix[end_i][end_j]
            
            if mid == start:
                return mid_val == target or end_val == target
            
            else:
                if mid_val==target:
                    return True
                elif mid_val<target:
                    return binarySearch(mid+1, end)
                else:
                    return binarySearch(start, mid-1)

        return binarySearch(0, mn-1)



                                                                                                                                                                                                                                                                                                        
