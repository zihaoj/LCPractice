'''
90. Subsets II
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


'''
same as the subset problem. But note here that we would need to output without duplicates.
so build a dictionary first and then append based on the counts of each element
'''


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        counts = {}
        
        for n in nums:
            counts[n] = counts.get(n, 0)+1
                                                    
            
        output = [[]]
            
        for n in counts:
            tmp = []
            for o in output:
                for i in xrange( counts[n] ):
                    tmp.append( o+[n]*(i+1) )
                        
            output = output + tmp
                        
    return output            
