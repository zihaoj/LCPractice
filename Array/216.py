'''
216. Combination Sum III
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
'''


'''
use recursion
note: every time pass in one list to the next step and if satisfies the requirement add to the solution; Don't over think about the problem
Shrink the tree size for each search. 
Note carefully about the k value 
'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        results = []
        
        def recurse( k , n, left, parent):
            if k == 1:
                if n in range(left, 10):
                    result = parent + [n]
                    results.append( result )
                    
                else:
                    thissum = sum(parent)
                                                                                            
                    for i in xrange(parent[-1]+1, n+1):
                        recurse(k-1, n-i, i+1, parent+[i])
                    
        for s in range(1,10):
            recurse(k-1, n-s, s+1, [s])
                            
        return results
