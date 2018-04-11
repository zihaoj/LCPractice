'''
244. Shortest Word Distance II
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.
'''

'''
if we don't want to count the dictionary building time, and only count access time, we should pre-build dict for all pairs then access takes O(1)
otherwise, build location ditionary and given a pair loop through the locations and calculate the difference. This would go as O(m+n)
'''



class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        
        self.location = {}
        self.len = len(words)
        
        
        for i, w in enumerate(words):
            if w not in self.location:
                self.location[w] = [i]
            else:
                self.location[w].append(i)
                                                                                
                
    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        p1 = self.location[word1]
        p2 = self.location[word2]
        
        i = 0
        j = 0
        
        shortest = self.len + 1

        while i< len(p1) and j<len(p2):
            shortest = min(    shortest, abs(p1[i]-p2[j])    )
            
            if p1[i]< p2[j]:
                i+= 1
            else:
                j+= 1
                
    return shortest
            
            
            
            
            
            
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
