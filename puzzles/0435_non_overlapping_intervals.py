"""

72. CLOSED (1) Non-overlapping Intervals - LeetCode

Given an array of intervals `intervals` where `intervals[i] = [start``i``, end``i``]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:

    Input: intervals = [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:

    Input: intervals = [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Constraints:

- `1 <= intervals.length <= 10``5`
- `intervals[i].length == 2`
- `-5 * 10``4` `<= start``i` `< end``i` `<= 5 * 10``4`

SOLUTION ATTEMPT
first let’s sort all intervals on ther lower
interval s= sorted(intervals, key= lambda interval: interval.start)
identify which interval overlaps with which: see this as an undirected graph, we want to make the graph such that the node with the most neighbours falls out first (not pers se the longest one), decrease all neighbours with .

sort all nodes based on their number of neighbours, decrease by 1 the neighbourcount of all neighbours, and continue until all are disconnected.

Worst case this would be N^N running time: i.e: [[1,2], [1,2], [1,2] … [1,2]] and N^2 space
(adjacency matrix). I think we can make this N^2 in time and space if we use the adjacency matrix correctly
"""