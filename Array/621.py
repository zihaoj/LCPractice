'''
621. Task Scheduler
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.
You need to return the least number of intervals the CPU will take to finish all the given tasks.

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

'''



class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        '''
        key is that we should schedule the most frequent task in remaining set 
        whenever it has passed the cooling period
        as we don't need to ouput the actual sequence
        we just need to keep the number of tasks
        (1) use max heap to keep track of the next biggest one
        (2) segment the sequence into periods of length n+1, the first task will be the one with biggest remaining counts
        then need to decrease the first [1:n+1] task counts by 1 as well            
        (3) python does not have max heap. But can use min heap and negative values to work it out         
        '''
        
        task_dict = {}
        for t in tasks:
            if t in task_dict:
                task_dict[t] += 1
            else:
                task_dict[t] =1
                
        heap = []
        for t in task_dict:
            heapq.heappush( heap, -task_dict[t])
                    
        period = n+1
        count = 0
                    
        while heap != []:
                        
            tmp_list = []
                        
        
            dec = 0
            for i in range( min(period, len(heap) )  ):
                tmp_list.append( heap.pop(0)+1)
                dec += 1

            for t in tmp_list:
                if t <= -1:
                    heapq.heappush(heap, t)
                        
            count += period if len(heap)!=0 else dec
                        
        return count
                
                                                                                                                                                                                                                                                                                                        
