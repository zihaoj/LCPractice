'''
729. My Calendar I
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

'''


'''
use BST to do the work. 
Just rememeber the nodes could contain more things than just one number
'''


class BSTNodes:

    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.lneighbor = None
        self.rneighbor = None
        

class MyCalendar(object):
    
    def __init__(self):
        
        self.root = None
        
        
    def BSTSearch(self, node, start, end):
        
        if node.l >= end:
            if node.lneighbor:
                return self.BSTSearch(node.lneighbor, start, end)
            else:
                node.lneighbor = BSTNodes(start, end)
                return True
        elif node.r <= start:
            if node.rneighbor:
                return self.BSTSearch(node.rneighbor, start, end)
            else:
                node.rneighbor = BSTNodes(start,end)
                return True
        else:
            return False
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        if not self.root:
            self.root = BSTNodes(start, end)
        return True

    return self.BSTSearch(self.root, start, end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
