'''
80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        Best solution is O(n) time complexity and O(1) space
        if the current elment is larger than the nums[i-2], then we should increase the count and move this element ahead
        otherwise, it's a duplicate and needs to be removed by elements later
        '''
        i =0
        for n in nums:
            if i <2 or n > nums[i-2]:
                nums[i] = n
                i += 1
                
        return i

