'''
75. Sort Colors

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''

'''

A:
many ways to approach; with O(n) space we can just count and expand out the list
with O(1) space:
     first trial, two pass, loop through the list swap first 0's to the begining, then swap 2's to the end
     second approach: keep to counters of boundaries i, j for 0 and 1; loop over and fill elements according to boundaries;

'''



class Solution(object):
        def sortColors(self, nums):
                    """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """


        '''
        for i in range(len(nums)):
        
            if nums[i] ==0:
                nums[:i+1] = [0]+nums[:i]

        n = len(nums)
        for i in range(1, len(nums)):

            if nums[n-i-1] ==2:
                nums[n-i-1:] = nums[n-i:]+[2]
            #print i, nums
        '''
        i=0
        j=0

        for k in range(len(nums)):
            cache = nums[k]
            nums[k] =2

            if cache<2:
                nums[j]=1
                j+=1

            if cache<1:
                nums[i]=0
                i+=1

                                                                                                                                                                                        
