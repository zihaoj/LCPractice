'''
541. Reverse String II

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

'''

'''
same thought as reverse string, just need to discuss different cases. 
note:

(1) floor division //
(2) ceil division (a-1)//x+1
(3) str.join(list)
'''


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        
        nrev = len(s)//(2*k)
        mod  = len(s)%(2*k)
        
        
        for i in xrange(nrev):
            s[2*i*k:2*i*k+k] = s[2*i*k:2*i*k+k][::-1]
            
            if mod <= k:
                s[2*nrev*k:  ] = s[2*nrev*k:][::-1]
            else:
                s[2*nrev*k: 2*nrev*k+k ] = s[2*nrev*k: 2*nrev*k+k][::-1]

        return "".join(s)
