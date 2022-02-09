"""

4. CLOSED Container With Most Water - LeetCode

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i``th` line are `(i, 0)` and `(i, height[i])`.
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)


i.e: [1, 8, 6, 3, 7, 3]:
(8, 6) would give 1*6 m^2
(8, 7) would give 3*6 m^2
(8, 3) would give 4*3 m^2
(x, y) would give len(y_idx-x_idx) * min(x, y) m^2
So. the goal is to find the maximal m^2.
SLOW version is just a double for loop and finding maximum area like that
FAST version would probably be O(NlogN) by the use of some sorting
example heights: [6, 4, 5, 2] → sorted [2, 4, 5, 6]
set bounds 0, n
now from the lowest we know the maximal can be only 2*max(index to bounds), e.g: maximally to the left or to the right
and now set bounds to: 0, index, n
now from the second lowest we know the maximal can only be 4*max_distance_to_bound)
etc.

then take max_area like that as well!

def find_biggest_area(heights):

    max_area = 0
    heights_sorted = sorted(heights)  # O(NlogN)
    heights_sorted_args = argsorted(height)  # O(NlogN)


    bounds = binaryTree([0, n])
    for i, h in zip(heights_sorted_args, heights_sorted);  # O(N)
        bound_right = bounds.findclosest_bigger(i, bounds)  # O(1)
        bound_left = bounds.findclosest_smaller(i, bounds)  # O(1)
        max_area_h= h * max(abs(i-bound_right), abs(i-bound_left))
        max_area = max(max_area, max_area_h)
        bounds.insert(i)  # O(log N)

    return max_area

This can be easily expanded to output the bounds as well…
O(N) in space complexity, O(NlogN) in time complexity.

"""