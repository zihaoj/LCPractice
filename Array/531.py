'''
531. Lonely Pixel I
Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.
'''

'''
key points are that we cannot do better than O(mn). Need to look through cols and rows for sure.
Then keep dicts for both cols and rows to count the number of 'B' in each row and col
Then output the min of row and cols with having 1 "B"
'''


class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        
        colcount = {}
        rowcount = {}
        
        for i in xrange(len(picture)):
            for j in xrange(len(picture[0])):
                if picture[i][j] == "B":
                    
                    rowcount[i] = rowcount.get(i, 0) +1
                    colcount[j] = colcount.get(j, 0) +1
                    
                    col_uniq = 0
                    row_uniq = 0
                    
        for c in rowcount:
            if rowcount[c] ==1:
                row_uniq += 1
                            
        for c in colcount:
            if colcount[c] ==1:
                col_uniq += 1
                

        return min(col_uniq, row_uniq)

                                                                                                                                                                                                                                                        
