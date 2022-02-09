"""

CLOSED  Number of Islands - LeetCode

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:

    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3


Constraints:

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

All four edges surrounded by water: by using another matrix we can …
A “1” already belongs to an existing island if the cell to the left or up, already belong to an island (assuming we are iterating from 0,0): This requires us to store an O(M) size previous row with the previous island assignments!

a helper function is usefull:
nxm grid!
def is_water(i, j):

    if 0< i < n-1 and 0< j < m-1:
        return grid[i, j] == 0
    return True

def is_land(i, j):

    return not is_water(i, j)

[0, 0, 0, 1, 1, 1]
[1, 0, 1,  1, 1, 1], blue is running_queue, purple is index under consideration

def calc_num_islands():


    num_islands = 0
    runrow_assignm_queue = deque([False]*m, max_len=m)  # filled with -1 first (water
    for i in range(n):
        for j in range(m):
            if is_water(i, j):
                runrow_assignm_queue.append_left(False)
                continue


            if runrow_assignm_queue[-1] == -1 and runrow_assignm_queue[0] == -1: # left,up=water
                num_islands += 1
                runrow_assignm_queue.append_left(True)

NEVERMIND, THIS IS BEST WRITTEN USING RECURSION AND A DICTIONARY? is it?

FLOODFILL: continue to connect until you cannot find any new connections anymore

seen = set()  # a dictionary without keys;)
def flood_fill(i, j):

    if (i,j) in seen or is_water(i,j):  # is_water filters out of bounds as well!
        return
    set.add((i,j))
    flood_fill(i+1, j)
    flood_fill(i-1, j)
    flood_fill(i, j+1)
    flood_fill(i, j-1)

return seen > 0  # if a new island has been made


now continue with island2, but at an index that is not already seen… we can do this by using an extra array of size O(nxm) size . Using an extra ammount of space O(nxm) we can do this is O(nxm) time like so:

grid_seen = nxm False filled matrix

new_island = False
def fill_island(i, j):

    if grid_seen[i, j] or is_water(i,j):  # is_water filters out of bounds as well!
        return
    new_island = True
    grid_seen[i, j] = True
    flood_fill(i+1, j)
    flood_fill(i-1, j)
    flood_fill(i, j+1)
    flood_fill(i, j-1)

return new_island

count = 0
for i in range(n)

    for j in range(m)
        if fill_island(i, j):
            count += fill_island(i, j)


this will be O(nxm) time

"""