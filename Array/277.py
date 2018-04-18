'''
277. Find the Celebrity
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.
Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
'''

'''
Two cases:
(1) if the celebrity exists, since there is only one, we need only one loop to find it:
we loop over all people and ask if the person knows the next.
celebrity does not know anyone else, so the pointer will stop at him
(2) if the celebrity does not exit, then we need to check for the person we get from (1)
(a) if he happens to know anyone else and (b) if everyone knows him

'''


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        '''
        Two cases:
        (1) if the celebrity exists, since there is only one, we need only one loop to find it:
        we loop over all people and ask if the person knows the next.
        celebrity does not know anyone else, so the pointer will stop at him
        (2) if the celebrity does not exit, then we need to check for the person we get from (1)
        (a) if he happens to know anyone else and (b) if everyone knows him
        
        '''

        cand = 0
        for i in xrange(n-1):
            if knows(cand, i+1):
                cand = i+1
                
        for i in xrange(n):
            if cand != i and knows(cand, i):
                return -1
            
        for i in xrange(n):
            if cand != i and not knows(i, cand):
                return -1
        
        return cand
