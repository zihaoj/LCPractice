'''
Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
'''

'''
Important to realize that the integers are always less than the size of the array, 
Hence we can index them to be between 0 and n-1
Then we apply polarity to the existing array
'''

class Solution(object):
        def findDuplicates(self, nums):
                    """
        :type nums: List[int]
        :rtype: List[int]
        """

        results = []
        for x in nums:
            if nums[abs(x)-1]<0:
                results.append(abs(x))
            else:
                nums[abs(x)-1] = nums[abs(x)-1]*(-1)

        return results
