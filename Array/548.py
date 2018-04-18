'''
548. Split Array with Equal Sum

Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.


Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5.
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
'''


'''
First make a cumulative sum list. This takes O(n)
Then for every j, search for i such that we have the first two balance and make a hash map to store the possible and balanced sum. This should take O(n^2)
Then for every j, search for k as well take also O(n^2)
Cannot do better than O(N^2)
'''


class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        Sum = 0
        cumsum = []
        
        for num in nums:
            Sum+=num
            cumsum.append(Sum)

        n = len(nums)
        valid_j_left = {}
                                                                                                
        
        for j in xrange(3, n-2):
            valid_sum = set()
            for i in xrange(1, j-1):
                
                if cumsum[i-1] == cumsum[j-1] - cumsum[i]:
                    valid_sum.add(cumsum[i-1])
                    valid_j_left[ j  ] = valid_sum
                    
                    
        for j in xrange(3, n-2):
            for k in xrange(j+2, n):
                if cumsum[k-1]-cumsum[j] ==  cumsum[n-1]-cumsum[k]:
                    thissum = cumsum[k-1]-cumsum[j]
                    if  thissum in valid_j_left[j]:
                        return True

        return False


                                                                                                                                                                                                                                                                                                                                            
