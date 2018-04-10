'''
67. Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

'''
one pass; keep track of the carry over 
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

                    
        i = 0
        carry = 0
        output = ""
        while i<max(len(a), len(b)):
            this_a = int(a[-1-i]) if i <len(a) else 0
            this_b = int(b[-1-i]) if i <len(b) else 0


            this_sum =  this_a + this_b + carry
            output  = str(this_sum%2)[0] + output
            
            carry = 1 if this_a+this_b+carry>1 else 0
            i+=1
        if carry ==1:
            output = "1"+output
        
        
        return output
