def binary_search(sorted, target, left=None, right=None):
    """ Finds the indices corresponding the value of target assuming the array is sorted.
    Returns -1 if target not in sorted """
    if left is None:
        left = 0
    if right is None:
        right = len(sorted)

    if left > right:
        return -1

    center = (left+right)//2
    if sorted[center] == target:
        return center

    if sorted[center] < target:
        return binary_search(sorted, target, left=center+1, right=right)
    else:
        return binary_search(sorted, target, left=left, right=center-1)