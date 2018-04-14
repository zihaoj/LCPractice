'''
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

'''

'''
Binary search. Since we need to return -1 if no element found
Pay attention to corner cases for length 0 and 1
'''



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        '''
        Also use binary search
        
        '''
        
        
        def binarysearch( inlist, target, shift  ):
            
            if len(inlist) ==0:
                return -1
            
            if len(inlist) ==1:
                if inlist[0] == target:
                    return 0
            else:
                return -1
            
            if len(inlist) ==2:
                if inlist[0] ==target:
                    return shift
                elif inlist[1] == target:
                    return shift+1
                else:
                    return -1

            else:
                start =0
                end = len(inlist)-1
                mid =(start+end)/2
                
                if inlist[start]<inlist[mid]:
                    if ( inlist[start]<= target <= inlist[mid] ):
                        return binarysearch( inlist[0:mid+1], target, shift)
                    else:
                        return binarysearch( inlist[mid:], target, mid+shift)
                    
                elif inlist[end]>inlist[mid]:
                    if ( inlist[mid]<= target <= inlist[end] ):
                        return binarysearch( inlist[mid:], target, mid+shift)
                    else:
                        return binarysearch( inlist[0:mid+1], target, shift)
                    
                    
        return binarysearch(nums, target, 0)
                








                                                                                                                                                                                                                                                                        
