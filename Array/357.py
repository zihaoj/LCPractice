'''
357. Count Numbers with Unique Digits
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
'''


'''
easy counting for n = 0, return 1
for n>=1, the first digits takes 9 values the rest takes 9, 8, 7 etc. 
'''


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
    """
    :type n: int
    :rtype: int
        """
    

    def count(k):
        if k ==0:
            return 1
        
        else:
            total = 9
            for i in xrange(k-1):
                total = total *(9-i)
                
        return total

    return sum( count(i) for i in xrange(0,n+1) )

                                                                                                                                                
