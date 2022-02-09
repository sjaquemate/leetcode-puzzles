"""

57. CLOSED 252. Meeting Rooms · LeetCode (gitbooks.io)

Given an array of meeting time intervals consisting of start and end times`[[s1,e1],[s2,e2],...]`(si< ei), determine if a person could attend all meetings.
Example 1:

    Input:
    [[0,30],[5,10],[15,20]]
    Output: false

Example 2:

    Input:[[7,10],[2,4]]

    Output:true

SOLUTION ATTEMPT
@dataclass
class Interval:

    start: int
    end: int

def valid_meetings(intervals)

    intervals = sorted(intervals, key = lambda interval: interval.start)
    for interval1, interval2 in zip(intervals[:-1], intervals[1:]):
        if interval1.end > interval2.start:
            return False
    return True

"""