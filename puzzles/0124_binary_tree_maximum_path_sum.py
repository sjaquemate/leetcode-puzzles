"""


31. OPEN Binary Tree Maximum Path Sum - LeetCode

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the `root` of a binary tree, return the maximum path sum of any non-empty path.

Example 1:

![](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)

    Input: root = [1,2,3]
    Output: 6
    Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:

![](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)

    Input: root = [-10,9,20,null,null,15,7]
    Output: 42
    Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

BETTER SOLUTION ATTEMPT:

Combining the methods from below, we can think of something like:

[5, 2, 5]

max_sum = 0
def path_sum(root):

    if root is None:
        return 0

    l = path_sum(root.left)
    r = path_sum(root.right)

    max_single = max( max(l, r)+node.value, node.value )  # which path, right or left is bigger?
    max_top = max(max_single, l+r+node.value)  # the “bridge” option: l+r+node.value
    nonlocal max_sum
    max_sum = max(max_sum, max_top)

    return max_single

and our result is now: max_sum ;)



SOLUTION ATTEMPT:
start most left, go to parent and go to right, if root: go to right and go to parent
ASSUME TREE WITH ONLY LEFTS

def max_path(node, max_so_far, cur_max,):

    # cur max is only for going down the recursion, max_so_far is what we want to retrieve
    if node is None:
        return max_so_far

    cur_max = max(node.value, cur_max + node.value)
    max_so_far = max(max_so_far, cur_max)


    max_so_far = max_path(node.parent, max_so_far, cur_max)

    return max_so_far

max_path(most_left_node, max_so_far=most_left_node.value, cur_max=most_left_node.value)

NOW ALSO WITH RIGHTS

def max_path(node, max_so_far, cur_max, eval_parent=True, eval_left=True, eval_right=True):

    # cur max is only for going down the recursion, max_so_far is what we want to retrieve
    if node is None:
        return max_so_far

    cur_max = max(node.value, cur_max + node.value)
    max_so_far = max(max_so_far, cur_max)

    if eval_parent:  # split paths
        max_so_far = max_path(node.parent, max_so_far, cur_max, eval_parent = True, eval_left=False, eval_right=False)
        max_so_far = max_path(node.parent, max_so_far, cur_max, eval_parent = False, eval_left=False, eval_right=True)
    if eval_parent:
        max_so_far = max_path(node.left, max_so_far, cur_max, eval_parent=False, eval_left=True, eval_right=True)
    if evaluate_right:
        max_so_far = max_path(node.right, max_so_far, cur_max, eval_parent=False, eval_left=True, eval_right=True)
    return max_so_far

COMPLEXITY: In this way, this algorithm is will visit every node only once, with a trivial computation each time and is therfore O(N) in time and space complexity.

HOWEVER THIS IS STILL WRONSINCE THE SPLITTING OF THE PATHS MAKE IT IMPOSSIBLE FOR LEAFS TO GET TO EACHOTHER


Another interesting way is to calculate the maximum path, but in any case, this exercise is very similar. Reordering the tree (NlogN) does not work because you change the tree in its process. We want to solve this problem with recursion… The fact that we cannot repeat nodes mean if i.e: a left of a subtree is in a path, either its parent, or its . FACT if we want to write using recursion we have to either start on the most left or most right of the tree. Let’s start left
ASSUMPTIONS: if there is a left, there is also a right! A node only has access to its parent

IDEA: find all the longest traversals in the path, remember the cumsum of their values, and find longest path from max(cumsum), min(cumsum()), the order of the path does not matter at all! i.e:

QUESTION: How to find the biggest consequtive sum:
[0, 100, -1000, 0, 500, -100]  # values # answer should be 500
[0, 0, -1100, 1000, 500, -600]
[0,

[0, 100, -900, -900, -400, -500]  # cumsum
sum(i,j) = cumsum(j+1)-cumsum(i); i < j
then O(N^2) can find the biggest total
thus: maximum total is max(


Find the maximum cumsum, then find the first negative cumsum value where
At least we need somewhere with a cumsum > 0. This is our end/startpoint, then we need to traverse the array


argmax(running sum)
earliest non zero before argmax(running_sum)

[0, 60, 40, 90, 91, -1000, 0, -500]  # running sum, when starting at index=0
sum =
argmax(cumsum) = 3
earliest cumsum that is bigger than 0…
HINT Kadane’s Algorithm:


    def maxSubArraySum(a,size):

        max_so_far =a[0]
        curr_max = a[0]

        for i in range(1,size):
            curr_max = max(a[i], curr_max + a[i])
            max_so_far = max(max_so_far,curr_max)

        return max_so_far

in own words:
example:
[1, 5, -4, 7]
0 index
cur_max = 1
max_so_far = 1
1 index
cur_max = 6
max_so_far = 6
2 index
cur_max = 2
max_so_far = 6
3 index
cur_max = 9
max_so_far = 9

max_sub_array_sum(arr):

    size = arr
    max_so_far = arr[0]
    cur_max = arr[0]
    for i in range(1, size):
        cur_max = max(a[i], cur_max + a[i])  #

        max_so_far = max(max_so_far, cur_max)

So with this algorithm and all paths from end to end we can calculate this…
worst case, this is O(NlogN) (all leafs to )…. This complexity would be way way too much. We can keep this running sum on the go of course
M + M /2 + M /4 + M /8 … = N, basically M is N

start left

"""