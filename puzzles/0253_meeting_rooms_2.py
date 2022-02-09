"""

58. CLOSED Algorithm-and-Leetcode/253. Meeting Rooms II.md at master · Seanforfun/Algorithm-and-Leetcode · GitHub

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
For example, Given [[0, 30],[5, 10],[15, 20]], return 2.

SOLUTION ATTEMPT
@dataclass
class Interval:

    start: int
    end: int

We can check if there is a collision, but this we need to solve with recursion:

intervals = sorted(intervals, key = lambda interval: interval.start)
max_rooms = 0
def calc_meeting_rooms(index, cur_rooms=0, cur_end=float(‘-inf’)):

    if index > len(intervals)-1:
        return


    overlaps_with_previous = intervals[index].start >  cur_end
    if overlaps_with_previous:
        cur_rooms += 1
    else:
        cur_rooms = 1
    cur_end = max(cur_end, intervals[index.end])  # new end
    max_rooms = max(max_rooms, cur_rooms)

    calc_meting_rooms(index + 1, cur_rooms, cur_end)
"""