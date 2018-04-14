'''
153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
You may assume no duplicate exists in the array.
'''

'''
No duplicates we can use binary search.
Be carefuly with the length of the array. We could start with length 1 which we should return directly		                    
'''



class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def binarysearch( inlist ):
            
            #print inlist
            
            if len(inlist) ==1:
                return inlist[0]
            
            ## already sorted
            elif inlist[0]<inlist[-1]:
                #print "already sorted"
                return inlist[0]
                                                        
            elif len(inlist) == 2:
                #print "final"
                return min(inlist[0], inlist[1])

            else:
            start = 0
            end = len(inlist)-1
            mid = (start+end)/2
            
            #rint start, end, mid
            #print inlist[0:mid+1], inlist[mid:]

            if inlist[start] > inlist[mid]:
                return binarysearch( inlist[0:mid+1]  )
            
            else:
                return binarysearch( inlist[mid:]  )
            
        return binarysearch(nums)
