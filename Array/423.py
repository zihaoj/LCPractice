'''
423. Reconstruct Original Digits from English
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
'''


'''
important thing is to notice we can calculate the numbers based on the appearances of characters
'''


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        count = {}
        spells = ["zero","two","six","eight","seven","three","four","five","nine","one"]
        for w in spells:
            for sub in w:
                count[sub] =0
                
        for ch in s:
            count[ch] += 1
            
            count_n = {}
            count_n[0] = count["z"]
            count_n[1] = count["o"]-count["z"]-count["w"]-count["u"]
            count_n[2] = count["w"]
            count_n[3] = count["t"]-count["w"]-count["g"]
            count_n[4] = count["u"]
            count_n[5] = count["f"]-count["u"]
            count_n[6] = count["x"]
            count_n[7] = count["s"]-count["x"]
            count_n[8] = count["g"]
            count_n[9] = count["i"]-count["x"]- count["f"]+count["u"]-count["g"]
                    
        output = ""
        for i in xrange(10):
            output += str(i)*count_n[i]
            
        return output
                
