"""
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start``i``, end``i``]` represent the start and the end of the `i``th` interval and `intervals` is sorted in ascending order by `start``i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.
Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start``i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return `intervals` after the insertion.

Example 1:

    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

SOLUTION ATTEMPT:
with non-overlapping intevals, the lower indices are sorted, and the righter bounds as well.
Thus we can do a binary search on the lower bound,

binary_search_closest():

    # type left get smaller one !
    pass
    return closest_index, closest_value or return None

closest_left_index, _ = binary_search_closest(arr=interval[:, 0])  # logN
interval_left = None
if closest_left_index is not None:

    interval_left = intervals[closest_left_index]

if left > interval_left[1]:

    interval_left = None

closest_right_index, _ = binary_search_closest(arr=interval[:, 1])  # logN
interval_right = None
if closest_right_index is not None:

    interval_right = intervals[closest_right_index]

if right < interval_right[0]:

    interval_left = None

if interval_left is None and interval_right is None:

    intervals.insert(closest_left_index, interval)

elif interval_left is None:

    intervals[closest_right_index] = merge_intervals(interval, interval_right)

elif interval_right is None:

    intervals[closest_left_index] = merge_intervals(left_interval, interval)

else:

    intervals[closest_left_index] = merge_intervals(merge_intervals(left_interval, interval), interval_right)

This is the general idea, doesn’t look so nice but should work
"""