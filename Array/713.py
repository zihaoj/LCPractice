'''
713. Subarray Product Less Than K
Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

if array[i:end] works then anything within the array works 
'''


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        
        begin = 0
        end   = 0
        Sum =0
        prod =1
        
        while end < len(nums):
            if nums[end]<k:
                Sum += 1
                
                prod *= nums[end]
                
                
                if prod <k:
                    Sum += (end-begin)

            else:
                while prod>=k and begin<end:
                    
                    prod = prod/nums[begin]
                    begin += 1
                        
                Sum += (end-begin)

            end += 1

        return Sum
                
