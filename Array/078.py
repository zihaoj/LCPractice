class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
        unique_el = set()
        
        for x in nums:
            unique_el.add(x)
            
            results = [ [] ]
            
        for x in unique_el:
            add_on = [ [x]+a for a in results]
            results = results + add_on
                
        return results
