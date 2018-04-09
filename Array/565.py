'''
565
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.
Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

A:
use dfs nothing is fancy
'''


class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        Use DFS to search for connected components
        '''
        
        visited = set()
        max_count =0
        
        def dfs(start_element, array):
            nodes = [start_element]
            count = 0
            
            while nodes != []:
                node  = nodes.pop()
                neighbor = array[node]
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    nodes.append(neighbor)
                    count += 1
                    
                else:
                    return count
                
        for v in nums:
            if v not in visited:
                max_count = max(dfs(v, nums), max_count)
        return max_count
            
