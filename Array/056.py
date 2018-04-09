'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''


'''
sort first with lambda function
then just merge 

'''


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        if len(intervals) == 0:
            return []
        
        sorted_intervals = sorted( intervals, key=lambda x: x.start, reverse=False )
        new_list = [sorted_intervals[0]]
        
        for i in xrange(len(sorted_intervals)-1):
            
            if sorted_intervals[i+1].start <= new_list[-1].end:
                new_list[-1].end = max(new_list[-1].end, sorted_intervals[i+1].end)
                                                                                                    
            else:
                new_list.append( sorted_intervals[i+1]  )
                
                
        return new_list
