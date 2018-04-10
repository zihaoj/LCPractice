'''
370. Range Addition

Assume you have an array of length n initialized with all 0's and are given k update operations.
Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
Return the modified array after all k operations were executed.
'''

'''
A:
could use naive approach but takes O(k*n) 

two pass cumulative sum : O(k+n)
for an array that has  A[start] += inc and A[end+1] -= inc
second path keep a sum and fill in the new array with the cumulative sum        
'''
        


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """

        
        tmp = [0]*length
        for update in updates:
            start, end, inc = update
            tmp[start] += inc

            if end+1<length:
                tmp[end+1] -= inc
                
        cumulative = 0
                
        for i, n in enumerate(tmp):
            cumulative += n
            tmp[i] = cumulative
            
        return tmp
                                                                                                                                                        
                                                                                                                                                    
