'''
769. Max Chunks To Make Sorted
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?


Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
'''



'''
go through the list once, 
we use induction, 
a subarray can be sorted together iff max(subarray) == len(subarray)
otherwise some larger element from later part of the array is mixed in and we will have to bring that to the end. 
'''

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        
        
    
        Max =-1
        count = 0
        for i, a in enumerate(arr):
            Max = max(Max, a)
            if Max == i:
                count += 1
        return count
            
