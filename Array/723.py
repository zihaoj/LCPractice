'''
723. Candy Crush
This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the current board.

'''

'''
Algorithm goes into two parts:
(1) First mark all the points which can be crashed
    Have to loop through all colums and rows and find three consecutive pixels

(2) Second apply the gravity:
    This can be done using the same algorithm as Dutch Flag color partition i.e. keep the partition pointer 
'''


class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """

        def crush(board):
            rows = len(board)
            cols = len(board[0])
            done = True
            
            mask = [[ 0 for i in range(cols) ] for j in range(rows)]
            
            # first mark all pixels need to be crashed in rows
            
            for i in xrange(rows):
                for j in xrange(cols-2):
                    if (board[i][j] == board[i][j+1] == board[i][j+2] != 0):
                        done = False
                        mask[i][j]   = 1
                        mask[i][j+1] = 1
                        mask[i][j+2] = 1
                        
            # then mark all pixels need to be crashed in cols
                        
            for i in xrange(rows-2):
                for j in xrange(cols):
                    if (board[i][j] == board[i+1][j] == board[i+2][j] != 0):
                        done = False
                        mask[i][j]   = 1
                        mask[i+1][j] = 1
                        mask[i+2][j] = 1

            # apply gravity step for each column, can use the same algorithm as the dutch flag partition problem
            for j in xrange(cols):
                partition = 0
                for i in xrange(rows):
                    cache = board[-1-i][j]
                    board[-1-i][j] =0
                    if mask[-1-i][j] ==0:
                        board[-1-partition][j] = cache
                        partition += 1
                        
            if done:
                return board
            else:
                return crush(board)
                        
        return crush(board)


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
