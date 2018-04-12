'''
611. Valid Triangle Number
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

'''

'''
impossible to do better than O(n^2)
so just sort first 
then we need to satisfy one constraint which is a+b>c. 
start scanning i,j,k with j= i+1 and k=i+2. Stop if nums_[k] cannot satisfy the requirement there. 
for a particular pair of i,j, we have k-j-1 combinations
need to really pay attention to case where i, j =0. So always start scanning with k at least as large as j+1
'''

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n  = len(nums)
        if n<=2:
            return 0
        
        nums_sort = sorted(nums)

        count = 0
        k = 2
        
        for i in xrange(n-2):
            k = i+2
            for j in xrange(i+1,n-1):
                
                a = nums_sort[i]
                b = nums_sort[j]
                k = max(k, j+1)
                while k<n and  nums_sort[k]<a+b:
                    k+= 1
                count += k-j-1
                    
        return count
                                                                                                                                                                                                                                                                        
