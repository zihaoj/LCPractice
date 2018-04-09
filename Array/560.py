

'''
560. Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
'''


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        '''
        Two ways to do:
        (1) is to keep the cumulative sum and loop over all sub arrays, taking O(n^2) time and O(1) space
        (2) is to use hash map to record the sum of elements up to nums[i]
        
        we can find subarrays with sum k by checking nums[i]-nums[j]==k for j<i
        
        '''

        sum_dict = {0:1}
        count = 0
        cumulative = 0
        
        for n in nums:

            cumulative  += n
            diff = cumulative-k
            count += sum_dict.get(diff ,0)
            
            sum_dict[cumulative] = sum_dict.get(cumulative, 0) + 1
            
            
            print sum_dict
        return count
