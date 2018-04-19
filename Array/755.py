'''
755. Pour Water

We are given an elevation map, heights[i] representing the height of the terrain at that index. The width at each index is 1. After V units of water fall at index K, how much water is at each index?

Water first drops at index K and rests on top of the highest terrain or water at that index. Then, it flows according to the following rules:

If the droplet would eventually fall by moving left, then move left.
Otherwise, if the droplet would eventually fall by moving right, then move right.
Otherwise, rise at it's current position.
Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction. Also, "level" means the height of the terrain plus any water in that column.
We can assume there's infinitely high terrain on the two sides out of bounds of the array. Also, there could not be partial water being spread out evenly on more than 1 grid block - each unit of water has to be in exactly one block.

'''


'''
The algorithm just goes as the description says:
For every droplet at index i, we check for [0,i-1] see where the minimum height is and put the droplet there.
Then we check for [i+1,end] see where the minimum heigh is and put the droplet there       
'''


class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        
        
        '''
        The algorithm just goes as the description says:
        For every droplet at index i, we check for [0,i-1] see where the minimum height is and put the droplet there.
        Then we check for [i+1,end] see where the minimum heigh is and put the droplet there       
        
        '''
        
        
        for i in xrange(V):
            minLeft = heights[K]
            minRight = heights[K]
            
            minLeft_ind  = -1
            minRight_ind = -1
            
            ## Search left, and stop if meet a wall
            for j in xrange(K):
                if heights[K-j-1]< minLeft:
                    minLeft = heights[K-j-1]
                    minLeft_ind = K-j-1
                elif heights[K-j-1]> minLeft:
                    break
                
                if minLeft_ind >=0:
                    heights[minLeft_ind] +=1
                    continue
                
            ## Search right, and stop if meet a wall
            for j in xrange(K+1,len(heights)):
                if heights[j]< minRight:
                    minRight = heights[j]
                    minRight_ind = j
                elif heights[j]> minRight:
                    break

                if minRight_ind >=0:
                    heights[minRight_ind] +=1
                    continue

            ## cannot go anywhere then just stay
            heights[K] +=1
        return heights









                                                                                                                                                                                                                                                                                                                                                                
