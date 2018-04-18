'''
39. Combination Sum

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
'''


'''
Use DP and loop over the list many times
Then the key is to realize that to avoid duplicates, we need to maintain an
order strucutre in the constructed sequence 
If we sort the candidates and constatnly compare it to the last element 
of the current accumulated list, then naturally avoid duplicates
'''


class Solution(object):
    def combinationSum(self, candidates, target):
        
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        cand = sorted(candidates)
        
        output = []
        
        def recurse( cand_set, target, acc):
            
            if target == 0:
                output.append(acc)
                return
            elif len(cand_set)==0:
                return
            else:

                for v in cand_set:
                    if v>target:
                        continue
                    if len(acc)>0 and v<acc[-1]:
                        continue
                    recurse(cand_set,  target-v,  acc+[v])
                    

        recurse(  cand, target, [])

                                                                                                                                                                                                                return output
                                                                                                                                                                                                                                    
