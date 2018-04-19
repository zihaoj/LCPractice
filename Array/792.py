'''
792. Number of Matching Subsequences

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.


Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].

'''


'''
keep a dictionary for words and which letter they are waiting for        
then if we see the needed first word, elimnate that first letter 
and re-organize the dictionary
If the word has length one and meet its needed letter then we can 
increment the counter
'''


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        # initialize a dictionary with the first letter
        firstletter = {}
        
        for c in [chr(i) for i in range(ord('a'),ord('z')+1)]:
            firstletter[c] = []
            
            for w in words:
                firstletter[ w[0] ].append( w )
                
                count = 0
                
                for c in S:
                    tmp_set_thisletter =[]
                    
                    for w in firstletter[c]:
                        
                        if len(w) ==1:
                            count += 1
                        else:
                            if w[1] == c:
                                tmp_set_thisletter.append(w[1:])
                            else:
                                firstletter[w[1]].append( w[1:] )

            firstletter[c]  = tmp_set_thisletter
        return count

                                                                                                                                                                                                                                                





