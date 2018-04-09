class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        
        '''
        def fact(x):
    
            if x ==1 or x==0:
                return 1
            
            out = x
            for a in xrange(1, x):
                out *= a
            
            return out

        return fact(m+n-2)/( fact(m-1)*fact(n-1)  )
        '''

        '''
        just practice dp as well
        '''


        table = [[1 for i in range(n)] for j in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                table[i][j] = table[i-1][j] + table[i][j-1]
        return table[m-1][n-1]




                                                                                                            
