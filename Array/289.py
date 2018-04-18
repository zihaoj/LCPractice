'''
289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
'''


'''

so we need four coding basically:
0  = dead->dead
1  = live->live
2  = dead->live
3  = live->dead        

Then use list comprehension for better representation of the neighbors.
We can include the point itself than subtract it

'''


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        

        if board == []:
            return []


        m = len(board)
        n = len(board[0])

        for i in xrange(m):
            for j in xrange(n):
                
                count = sum( [board[p][q]%2  for p in range(max(0,i-1), min(m,i+2)) for q in range(max(0,j-1), min(n,j+2)) ]  ) - board[i][j] %2
                if (count < 2 or  count> 3)and board[i][j]%2 ==1:
                    board[i][j] = 3
                elif (count ==2 or count ==3) and board[i][j]%2 ==1:
                    board[i][j] = 1
                elif count ==3 and board[i][j]%2 ==0:
                    board[i][j] = 2
                    

        #print board
        for i in xrange(m):
            for j in xrange(n):
                if  board[i][j] == 3:
                    board[i][j] =0
                if  board[i][j] == 2:
                    board[i][j] =1
