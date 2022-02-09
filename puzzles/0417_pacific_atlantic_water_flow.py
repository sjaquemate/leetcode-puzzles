"""

70. CLOSED  (1) Pacific Atlantic Water Flow - LeetCode

There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates `result` where `result[i] = [r``i``, c``i``]` denotes that rain water can flow from cell `(r``i``, c``i``)` to both the Pacific and Atlantic oceans.

Example 1:

![](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)

    Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:

    Input: heights = [[2,1],[1,2]]
    Output: [[0,0],[0,1],[1,0],[1,1]]


Constraints:

- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10``5`


What is we call each cell a node, and calculate which cells we can go towards, if we know cell c(i,j) cannot reach a part, also make an ocean_node and pacififc_node. In effect we have created a directed graph. But we can also direct it in the up direction, in a way we check if from an ocean if we can reach a node, Now the question is, can from node ni,j we reach pacific? (and atlantic?)

Then we will start with ocean_node, and:

creating the nodes
ocean = Node()
pacific = Node()
nodes = {}
for i in range(n):

    for j in range(m):
        node = Node(val = matrix[i,j])
        if i == 0 or j ==0:
            ocean.up.append(node)
        if i == n-1 or j == m-1:
            pacific.up.append(node)
        nodes[(i,j)] = node

for i in range(n):

    for j in range(m):
        node = node[(i, j)]
        if i-1>=0 and nodes[(i-1,j)].val > node.val:
            node.up.append(nodes[(i-1, j)])
        ..etc..


def calc_reachable(node):

    seen = set()
        def traverse_upstream(node):
            if node in seen:
                return
            seen.add(node)
            for child in node.up:
                traverse_upstream(node)
    return seen

reach_ocean = calc_reachable(ocean_node)
reach_atlatntic = calc_reachable(atlantic_node)
return reach_cocean.intersection(reach_atlantic)
This runs in O(mxn) time and space
"""