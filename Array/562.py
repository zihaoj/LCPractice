'''
562. Longest Line of Consecutive One in Matrix

Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3

'''


'''
Use DP. Keep table of four elements. 
One for continuous row up to [i,j]. One for col, one for diag and one for anti-diag
My sol could be simplified somewhat more. No need to initialize the first row
'''


class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        
        if M ==[]:
            return 0

        
        m = len(M)
        n = len(M[0])
    

        Max = 0
        table = [   [  [0,0,0,0] for i in xrange(n) ] for j in xrange(m) ]
        
        
        # row  0
        # col  1
        # diag 2
        # anti 3
        
        if M[0][0] ==1:
            table[0][0] =[1,1,1,1]
            Max = 1
        else:
            table[0][0] =[0,0,0,0]
            
            
            ### fill the first row
            
        for j in xrange(1, n):
            if M[0][j]:
                table[0][j][0] = 1+ table[0][j-1][0]
                table[0][j][1] = 1
                table[0][j][2] = 1
                table[0][j][3] = 1

                Max = max(Max, max(table[0][j]))

        for i in xrange(1, m):
            for j in xrange( 0, n ):
                if M[i][j]:
                    
                    
                    ### row and diagnal update
                    if j !=0:
                        table[i][j][0] = 1+ table[i][j-1][0]
                        table[i][j][2] = 1+ table[i-1][j-1][2]
                    else:
                        table[i][j][0] = 1
                        table[i][j][2] = 1
                        
                        
                    ### Anti diagnoal
                    if j!=n-1:
                        table[i][j][3] = 1 + table[i-1][j+1][3]
                    else:
                        table[i][j][3] = 1

                    #### Column update
                    table[i][j][1] = table[i-1][j][1] +1

                    Max = max( Max, max(table[i][j])   )

    return Max
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

