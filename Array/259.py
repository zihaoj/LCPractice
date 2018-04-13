'''
259. 3Sum Smaller
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
For example, given nums = [-2, 0, 1, 3], and target = 2.
Return 2. Because there are two triplets which sums are less than 2:
'''

'''
Sort takes O(nlogn), so let's do it
Then it's a matter of increment i, j. Same problem as the three segements for triangle
Do a reversed scan of k
'''



class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        n = len(nums)
        if n<= 2:
            return 0
        
        sort_nums = sorted(nums)
        count = 0
        
        for i in xrange(n-2 ):
            k = n-1

            for j in xrange(i+1, n-1):
        
                a = sort_nums[i]
                b = sort_nums[j]
            
                while k>j+1 and a+b+sort_nums[k]>= target:
                    k = k-1
                    
                if a+b+sort_nums[k]<target:
                    count += k-j

        return count





                                                                                                                                                                                                                                            
