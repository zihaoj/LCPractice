'''
533. Lonely Pixel II
Given a picture consisting of black and white pixels, and a positive integer N, find the number of black pixels located at some specific row R and column C that align with all the following rules:

Row R and column C both contain exactly N black pixels.
For all rows that have a black pixel at column C, they should be exactly the same as row R
The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

'''


'''
since we need the exact patterns of the rows, 
we need to use hash map for the patterns which satsfy the row count requirement
for the full loop we also store all the column counts

then loop through all the patterns and see which columns satisfy the N counts
for each column satisfying the requirement count += N
'''


class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        
        
        dict_col  = {}
        dict_row  = {}
        
        count = 0
        for i in xrange(len(picture)):
            Nb_row = 0
        
            for j in xrange(len(picture[0])):
            
                if picture[i][j] =="B":
                    Nb_row += 1
                    dict_col[j] = dict_col.get(j, 0) + 1
                    
            if Nb_row == N:
                dict_row[ tuple(picture[i]) ] = dict_row.get( tuple(picture[i]), 0 ) + 1
                        
        for pat in dict_row:
            if dict_row[pat] != N:
                continue
                            
            for i in xrange(len(pat)):
                if pat[i] == "B" and dict_col[i] == N:
                    count += N
                                    
                                    
        return count
                                                                                                                                                                                                                                                                                                            
