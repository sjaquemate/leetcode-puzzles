"""

66. CLOSED 323 Number of Connected Components in an Undirected Graph · LeetCode solutions (gitbooks.io)

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.


    Example 1:
         0          3
         |          |
         1 --- 2    4
    Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

    Example 2:
         0           4
         |           |
         1 --- 2 --- 3
    Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

    Note:
    You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Keep a dictionary of seen as follows:

Node

    neighbours: List[Node]

seen = set()
traverse_edges(node):

    if node in seen:
        return
    seen.add(node)
    for child in node.children:
        traverse_edges(child)


num_connected = 0
for node in nodes:

    if node not in seen:  # this was not connected to anything before: is a new component
        traverse_edges(node)
        num_connected += 1
"""