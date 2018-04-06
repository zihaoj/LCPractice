'''
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?


'''

'''
constructive DP with memorization
search for permutations which would work

tuple is immutable hence hashable
set is mutable hence not hashable !!!!!
enumerate gives both index and object
'''


class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        cache = {}
        def recurse (i, X):
            
            count = 0
            
            if i ==1:
                count =1
            else:
                for j, x in enumerate(X):
                    if (i,X) not in cache:
                        new_set = X[:j] +X[j+1:]
                        
                        if i%x ==0 or x%i==0:
                            count += recurse( i-1, new_set)
                            
                    else:
                        count = cache[(i,X)]
                            
                cache[(i,X)] = count
            return count
                        
        return recurse(N, tuple(range(1,N+1)))


                                                                                                                                                                                                                                
