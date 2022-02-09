"""

14. CLOSED Spiral Matrix - LeetCode

Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.
Example 2:

![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

SOLUTION ATTEMPT:
We can use the get_ring method and do it sequentially like that, but we can also think of a nicer method.

select_right(arr, depth):

    i = depth
    return [(i, j) for j in range(depth, arr.shape[1]-1-depth)]

select_down(arr, depth):

    j = arr.shape[1] -1 -depth
    return [(i, j) for i in range(depth, arr.shape[0]-1-depth)]

select_left(arr. depth):

    i = arr.shape[0] -1 - depth
    return [(i, j) for j in range(arr.shape[1]-1-depth, depth)]

select_up(arr, depth):

    j = depth
    return [(i, j) for i in range(arr.shape[0]-1-depth, depth)]

Or something like this

"""