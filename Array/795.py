'''
795. Number of Subarrays with Bounded Maximum

We are given an array A of positive integers, and two positive integers L and R (L <= R).
Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.
Example :
Input: 
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Note:
L, R  and A[i] will be an integer in the range [0, 10^9].
The length of A will be in the range of [1, 50000].
'''


'''
Mis-understood the problem at first hand
We keep expanding the array with all elements <=R
We should notice that for any element >R, the counting of consecutive subarrays will stop
For a given subarray M, if an element is less than L, it could be combined with some near by element which is in between L and R
Therefore, we should count the number of continuous subarrays K with less than L within each subarray that only contains 
elements less than R. Then subtract K from the number of continuos sybarrays in M. 
'''


class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        
        
        count =0
        count_less_subarray = 0
        lessThanR = 0
        lessThanL = 0
        
        for n in A:
            
            if n >R:
                count += lessThanR*(lessThanR+1)/2 - count_less_subarray - lessThanL*(lessThanL+1)/2
                #print n, lessThanR, count
                
                lessThanR = 0
                lessThanL = 0
                count_less_subarray = 0
                
                
            else:
                if n>= L:
                    count_less_subarray += lessThanL*(lessThanL+1)/2
                    lessThanR += 1
                    lessThanL = 0
                    
                if n<L:
                    lessThanR += 1
                    lessThanL += 1
                    
        count += lessThanR*(lessThanR+1)/2 - count_less_subarray - lessThanL*(lessThanL+1)/2
                    
        return count
