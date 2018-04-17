'''
731. My Calendar II
Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

'''

'''
The problem seems easy but has a lot tricks
Pay attention to the details. It says no two conflict booking. It's ok to have C overlaps with A and B, while A and B do not overlap
Can only solve it in O(n^2) haven't seen better answers
Idea is to keep track of the current overlaps and the current calendar. 
'''


class MyCalendarTwo(object):
    
    def __init__(self):
            
        self.overlaps = []
        self.calendar = []
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        
        
        for overlap in self.overlaps:
            if end<= overlap[0] or start>=overlap[1]:
                continue
            else:
                return False
            
            
        for c in self.calendar:
            if start<c[1] and end>c[0]:
                self.overlaps.append( (  max(start,c[0]), min(end, c[1]))  )
                
                
        self.calendar.append( (start, end))
        return True
                
            
                # Your MyCalendarTwo object will be instantiated and called as such:
                # obj = MyCalendarTwo()
                                                                                                                                            # param_1 = obj.book(start,end)
