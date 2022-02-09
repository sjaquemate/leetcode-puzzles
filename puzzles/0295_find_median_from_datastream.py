"""

63. CLOSED (1) Find Median from Data Stream - LeetCode

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.
- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the MedianFinder class:

- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within `10``-5` of the actual answer will be accepted.


Example 1:

    Input
    ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    [[], [1], [2], [], [3], []]
    Output
    [null, null, null, 1.5, null, 2.0]

    Explanation
    MedianFinder medianFinder = new MedianFinder();
    medianFinder.addNum(1);    // arr = [1]
    medianFinder.addNum(2);    // arr = [1, 2]
    medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3);    // arr[1, 2, 3]
    medianFinder.findMedian(); // return 2.0


Constraints:

- `-10``5` `<= num <= 10``5`
- There will be at least one element in the data structure before calling `findMedian`.
- At most `5 * 10``4` calls will be made to `addNum` and `findMedian`.

SOLUTION ATTEMPT
Let’s think of space complexity: can we find the median without having stored all nums? → No, so space O(n), then let’s think of time complexity for adding and finding. if we have a balanced binary search tree, or any sorted list : we can do find median in O(1). To add a number to a balanced binary search tree it takes logN, thus time of adding an array of N is NlogN, (makes sense, since it’s sorted)

class MedianFinder:

    values: List[int]


    find_median():
        length = len(values)
        if length % 2 == 1:
            return values[length//2]
        return (values[length//2-1]+values[[length//2])/2

    add_num(num):
        index = find_closest(num)
        values.insert(index)

    find_closest_index(num, start=0, end=None):
        # use binary search as deatiled before, split up in get middle, value, if bigger repeat same  right if smaller repeat same left. stop if len(arr) == 0, that index
        if end is None:  # init
            end = len(values)-1
        length = end-start
        if length == 0 or length== 1
            return start  # still to test by example
        center = start+length//2
        if num > values[center]:
            return find_closest_index(num, start=center, end=end)
        else:
            return find_closest_index(num, start=start, end= center)
"""