'''
40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
'''


'''
need sorted arrays to improve the running time
use DP recurse on the smaller subset to find the good sum
use set to return no duplicates events
'''



class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candsort = sorted(candidates)
        
        outputs = set()
        

        def recurse(restcand, cumsum, path ):
            
        if len(restcand) ==0:
            return
        
        else:
            
            for i in xrange(len(restcand)):
                
                #print restcand[i], restcand
                
                if cumsum + restcand[i]== target:
                    #outputs.append( path+[restcand[i]]  )
                    outputs.add( tuple(path+[restcand[i]]) )
                
                elif cumsum + restcand[i] > target:
                    break
                
                else:
                    recurse ( restcand[i+1:], cumsum+restcand[i], path+[ restcand[i] ]  )
                    
        recurse( candsort, 0, []  )
        outlist =[ list(out) for out in outputs  ]
        return outlist
                                                                                                                                                        
