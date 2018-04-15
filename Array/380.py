'''
380. Insert Delete GetRandom O(1)

Design a data structure that supports all following operations in average O(1) time.
insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
'''

'''
Key is the getRandom operation. For set we can already do insert and delete with O(1) time.
Random we need indexing and hence need a list for this
'''


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.pos = {}
        self.nums = []
        
        
        def insert(self, val):
            """
            Inserts a value to the set. Returns true if the set did not already contain the specified element.
            :type val: int
            :rtype: bool
            """
            if val not in self.pos:
                
                self.nums.append(val)
                self.pos[val] = len(self.nums)-1
                return True
            return False
        
        
        def remove(self, val):
            """
            Removes a value from the set. Returns true if the set contained the specified element.
            :type val: int
            :rtype: bool
            """
            
            if val in self.pos:
                last, idx = self.nums[-1], self.pos[val]
                self.nums[idx] = last
                self.pos[last] = idx
                self.nums.pop()
                del self.pos[val]
                
                return True
            return False
        
        
        def getRandom(self):
            """
            Get a random element from the set.
            :rtype: int
            """
            
            return random.choice( self.nums)
        
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
    
