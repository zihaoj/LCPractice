'''
523. Continuous Subarray Sum
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

'''


'''
looks easy but has a lot  corner cases

to deal with k==0, we need to count number of continuous 0's
to deal with k!=0, remember of check continuos 0's as well

in general use the same idea as keep sum up to i, and check all the remainders of A[:j] for j<i. 
If remainder[j] == remainder[i], then we found a sum. 

Important to initialize the map to have 1 count for remainder 0
'''

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        
        '''
        keep a map of remainder 0 to k-1
        
        '''
        
        if k==0:
            for i in range(len(nums)-1):
                if nums[i]==0 and nums[i+1]==0:
                    return True
                return False
            
        count = 0
        cumulative =0
        dict_remainder ={0:1}
        
        for i, n in enumerate(nums):
                
            cumulative += n
            remainder = cumulative % k
                
            if i>=1:
                if (nums[i-1]==0 and n==0):
                    return True
                else:
                    count += dict_remainder.get(remainder ,0)

            dict_remainder[remainder] = dict_remainder.get(remainder, 0) + 1
                    
            if count>0:
                return True
        return False
