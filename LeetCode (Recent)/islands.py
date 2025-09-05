def islands(grid):
    '''
    Notes and initial thoughts
    BFS to traverse the grid
    create an array of directions to explore around the current cell
    '''
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0   


    def bfs(row, col):
        queue = []
        visited.add((row, col))
        queue.append((row, col))

        while queue:
            row, col = queue.pop(0)
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for d_row, d_col in directions:
                shifted_row, shifted_col = row + d_row, col + d_col

                if (shifted_row in range(rows) and 
                    shifted_col in range(cols) and 
                    grid[shifted_row][shifted_col] == "1" and 
                    (shifted_row, shifted_col) not in visited):

                    queue.append((shifted_row, shifted_col))
                    visited.add((shifted_row, shifted_col))

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row, col) not in visited:
                bfs(row,col)
                islands += 1

    return islands



grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

print(islands(grid))