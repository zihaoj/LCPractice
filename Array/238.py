'''
238. Product of Array Except Self

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

'''



'''
two passes, remember to shift the products

'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        '''
        two passes, first get the products for list_1= [ a2, a2a3, a2a3, ..., a2a3...an]
        second pass to get list_2 = []
        
        
        '''
        
        prod = 1
        first_pass = []
        for i in range(len(nums)-1):
            
            prod *= nums[-(i+1)]
            first_pass.append(prod)

            print "first_pass", first_pass
            
            result = [ first_pass[-1]  ]

        prod = 1
            
        for i in range(len(nums)-2):
            
            prod *= nums[i]
            print prod, first_pass[-(i+2)]
            result.append( prod*first_pass[-(i+2)] )
        result.append( prod*nums[-2]  )
                
        return  result
