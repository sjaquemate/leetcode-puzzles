"""

12. CLOSED Rotate Image - LeetCode

You are given an `n x n` 2D `matrix` representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]


def get_ring(arr, depth):

    return [arr[(i, j)] for (i, j) in get_ring_indices(arr, depth)]

def set_ring(ring, arr, depth):

    for value, (i, j) in zip(ring, get_ring_indices(arr, depth)):
        arr[(i,j)] = val


get_ring_indices(arr, depth):

    indices = []
    height, width = arr.shape
    min_x, max_x = depth, width-depth
    min_y, max_y = depth, width-depth
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cur = (min_x, min_y)
    for step in steps:
        while cur[0] >= min_x and cur[0] <= max_x and cur[1] >= min_y and cur[1] <= max_y:
            cur[0] @= step[0]
            cur[1] @= step[1]
            indices.append(cur)

rotate_ring_90deg(ring):

    # [1, 2, 3, 6, 9, 8, 7, 4] → [7, 4, 1, 2, 3, 6, 9, 8[
    # length = 8
    # to rotate by: 8 // 4 * 1 = 2
    return shift(len(ring) // 4)


def shift(arr, steps):

    return arr[-steps:] + arr[:-steps]

max_depth = arr.shape[0]//2
for depth in range(0, max_depth):

    ring = get_ring(arr, depth)
    rotated_ring = rotate_ring_90deg(ring)
    set_ring(arr, depth, rotated_ring)

or use rotation matrix;)
"""