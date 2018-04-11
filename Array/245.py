'''
245. Shortest Word Distance III
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
word1 and word2 may be the same and they represent two individual words in the list.
For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.
'''

'''
Cache the previous seen word1 or word2
if word 1 = curr: and cache == word2, check length
elif word 2 = curr: and cache == word 1, check length
'''



class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        cache = ""
        diff = len(words)+1
        count = 0
        start = False

        for w in words:
            
            if w == word1:
                start = True
            
                if  cache ==word2:
                    diff = min(diff, count+1)
                    count = 0
                    cache = w

            elif w == word2:
                start = True
                
                if  cache == word1:
                    diff = min(diff, count+1)
                    count = 0
                    cache = w
                    
                    
            else:
                count += 1 if start else 0
                    
                    
                    
        return diff
                                                                                                                                                                                            
