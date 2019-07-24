# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0 # initialize number of islands
        
        for row in range(len(grid)): # iterate through entire input matrix
            for col in range(len(grid[0])):
                if (grid[row][col] == "1"):
                    count += 1 # if land found i.e. value is 1, increment count
                    queue = []
                    queue.append([row,col]) # create an queue and add this location
                    grid[row][col] = "0" # assign 0 to this location so that it is not considered as an land block again
                    
                    while(len(queue)): # iterate through queue finding newer land blocks adjacent to current land block
                        corr = queue.pop(0)
                        if((corr[0]-1 >= 0) and grid[corr[0]-1][corr[1]] == "1"):
                            grid[corr[0]-1][corr[1]] = "0"
                            queue.append([corr[0]-1,corr[1]])
                            
                        if((corr[0]+1 < len(grid)) and grid[corr[0]+1][corr[1]] == "1"):
                            grid[corr[0]+1][corr[1]] = "0"
                            queue.append([corr[0]+1,corr[1]])
                            
                        if((corr[1]-1 >= 0 ) and grid[corr[0]][corr[1]-1] == "1"):
                            grid[corr[0]][corr[1]-1] = "0"
                            queue.append([corr[0],corr[1]-1])
                            
                        if((corr[1]+1 < len(grid[0])) and grid[corr[0]][corr[1]+1] == "1"):
                            grid[corr[0]][corr[1]+1] = "0"
                            queue.append([corr[0],corr[1]+1])
        
        return count # return number of islands !!