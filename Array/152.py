'''
152. Maximum Product Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

'''


'''
modification of Kadane’s algorithm for largest sum

If we don't have negative values, it's obvious that we can just use Kadane's directly
i.e. define a variable localMax(i) to be the largest product up to i'th position
where localMax(i+1) = Max(localMax(i), num[i+1])
And we also keep a global largest value to be globalMax 

If we have the negative values, then we need to take care of the negative values as well
so we keep track of a minimum
'''




class Solution(object):
        def maxProduct(self, nums):
                    """
        :type nums: List[int]
        :rtype: int
        """




        maxLocal = nums[0]
        minLocal = nums[0]
        maxGlobal = nums[0]

        for v in nums[1:]:

        
            if v >0:
                maxLocal = max(v, maxLocal*v   )
                minLocal = min(v, minLocal*v   )

            else:
                maxLocal, minLocal = max(v, minLocal*v), min(v, maxLocal*v)
                maxGlobal = max(maxLocal, maxGlobal  )

        return maxGlobal


                                                                                                                        
