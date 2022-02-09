"""

17. CLOSED Merge Intervals - LeetCode

Given an array of `intervals` where `intervals[i] = [start``i``, end``i``]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example = [1, 8], [2, 5], [5, 6]
right_sort = [2, 5], [5, 6], [1, 8]  # this sorting does matter
left_sort = [1, 8], [2, 5], [5, 6]

OR what if we convert this to: start, length:
and we sort on start:
call this interval:
(1, s=7), (2, s=3), (5, s=1)  # O(N)

merged_intervals = []  # forward linked list
for interval in intervals:

    start_cur = interval[0]
    size_cur = interval[1]
    last_interval = merged_interval.get_last()
    start_last, size_last = last_interval
    if start_cur > start_last + size_last:
        merged_interval = merge_intervals(interval, last_interval)
        merged_intervals.set_last(merged_interval)
    else:
        merged_interval.add_to_end(interval)


Naive would be a O(N^2) solution where N are the number of intervals…
Starting naive from the right:

def merge_intervals(interval1, interval2):

    low1, high1 = interval1
    low2, high2 = interval2

    if high1 < low2:
        return [inverval1, interval2]

    merged_interval = (min(low1, low2), max(high1, high2))
    return [merged_interval]

etc.
"""