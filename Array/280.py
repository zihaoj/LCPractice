'''
280. Wiggle Sort
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
'''


'''
A:
initial trial, very shitty solution; Sort first then combine

second way:
note that we can do in O(n) time
if we are sorting less, i.e. a[i]<a[i+1], then the next sorting greater will make the swap iff a[i+2]>= a[i+1] and hence the currrent swap is still valid
'''
        


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        '''
        nums_sort = sorted(nums)
        
        for i in range( len(nums_sort)//2 ):
            nums[2*i]   = nums_sort[i]
            nums[2*i+1] = nums_sort[i+(len(nums_sort)-1)//2+1]
        
        if len(nums_sort) % 2==1:
            nums[-1] = nums_sort[(len(nums_sort)-1)//2]
        '''


        less = True
        for i in range(len(nums)-1):
            if less and nums[i]> nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif not less and nums[i]<nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            less = not less
