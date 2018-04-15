'''
162. Find Peak Element
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.
For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

'''

'''
Fastest should be binary search. 
Notice that if we look an element and the local trend is increasing, i.e. A[i]<A[i+1], then we should search on the RHS
Similarly for the case where A[i]>A[i+1], we search on the LHS
And this general strategy covers the cases where the array is in strickly ascending or descending order
'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

    
        '''
        use binary search
        '''
        
        
        
        def recurse(nums, shift):
            
            if len(nums) ==1:
                return shift
            
            elif len(nums) ==2:
                if nums[0]<nums[1]:
                    return shift+1
                else:
                    return shift
                                                                                            
            
            start = 0
            end   = len(nums)-1
            mid   = (start+end)/2
            
            if nums[mid]<nums[mid+1]:
                return recurse(nums[mid:], shift+mid  )
            else:
                return recurse(nums[0:mid+1], shift)

    return recurse(nums, 0)
        
        
        
