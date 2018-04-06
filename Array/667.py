'''
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.
'''


'''
for 1 to n-k-1 we don't do anything
for n-k+1 to n, we have [n-k, n, n-k+1, n-1, ...], we get difference k, k-1, k-2, to 1 etc. 
'''


class Solution(object):
        def constructArray(self, n, k):
                    """
        :type n: int
        :type k: int
        :rtype: List[int]
        """


        results = range(1, n-k)
        
        for i in range(k+1):
            if i %2 == 0:
                results.append( n-k+i//2)
            else:
                results.append( n-i//2  )

        return results

