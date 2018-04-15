'''
670. Maximum Swap
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
'''

'''
O(n) time solution, loop over once to record the Maxium from [i:end]
and then loop again to swap for the current event with the maximum in the rest of the 
array with the largest index
'''



class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        num = list(str(num))
        max_idx = (len(num)-1)*[-1]
        max_array = (len(num)-1)*[-1]
        cumulative = -1

        idx = len(num)
        
        for i in xrange(len(num)-1):
            
            if cumulative<  num[-1-i]:
                cumulative = num[-1-i]
                idx = len(num)-i-1
                
                max_array[-1-i] = cumulative
                max_idx[-1-i] = len(num)-i-1
                
            else:
                max_array[-1-i] = cumulative
                max_idx[-1-i] = idx
                
        for i in xrange(len(num)-1):
            if num[i]<max_array[i]:
                num[i], num[ max_idx[i] ] = num[max_idx[i]], num[ i ]
                break
            
        return int("".join(num))
        
        
        



                                                                                                                                                                                                
