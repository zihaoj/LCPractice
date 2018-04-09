'''
495. Teemo Attacking
In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemos attacking ascending time series towards Ashe and the poisoning time duration per Teemos attacking, you need to output the total time that Ashe is in poisoned condition.
You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.
'''


'''
this is rather easy
'''

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
        total_time = 0
        
        for it in xrange(len(timeSeries)-1):
            total_time += min( timeSeries[it+1] - timeSeries[it], duration)
            
        if len(timeSeries) !=0:
            total_time += duration
                
        return total_time
