'''
490. The Maze

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
'''

'''
equivalent to finding a connected components, just dfs
preprocess to expand maze to include boundary
be very careful with the statement. the ball can be rolled until it sees an obstacle.
one thought is that for rolling based boundary determination, better to use while and avoid tough indexing
'''


class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """


        '''
        equivalent to finding a connected components
        preprocess to expand maze to include boundary
        '''


        rows = len(maze)
        cols = len(maze[0])

        maze_new = [ [ 1 for i in xrange(cols+2)  ] for j in xrange(rows+2) ]

        for i in xrange(rows):
            maze_new[i+1][ 1:cols+1 ] = maze[i]
            

        start = tuple(start)
        destination = tuple(destination)
        
        visited =set()
                                                                                                    
        def dfs(start):
            queue = [start]
            while queue != []:
                v = queue.pop()
                visited.add(v)
            
                neighbors = []
            
                x = v[0]
                y = v[1]

                ### up
                roll_x = x+1
                while maze_new[roll_x][y+1] ==0:
                    roll_x -=1
                    neighbors.append( ( roll_x ,y ) )

                ### down
                roll_x = x+1
                while maze_new[roll_x][y+1] ==0:
                    roll_x +=1
                    neighbors.append( ( roll_x-2 ,y ) )

                ### right
                roll_y = y+1
                while maze_new[x+1][roll_y] ==0:
                    roll_y +=1
                    neighbors.append( ( x , roll_y-2 ) )

                ### left
                roll_y = y+1
                while maze_new[x+1][roll_y] ==0:
                    roll_y -=1
                    neighbors.append( ( x , roll_y ) )


                for n in neighbors:
                    if n not in visited:
                        queue.append(n)
                        if n ==destination:
                            return True

                return False

        return dfs(start)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
