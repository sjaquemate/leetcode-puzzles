"""

67. CLOSED (1) Counting Bits - LeetCode

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the number of `1`'s in the binary representation of `i`.

Example 1:

    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10

Example 2:

    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101


Constraints:

- `0 <= n <= 10``5`


Follow up:

- It is very easy to come up with a solution with a runtime of `O(n log n)`. Can you do it in linear time `O(n)` and possibly in a single pass?
- Can you do it without using any built-in function (i.e., like `__builtin_popcount` in C++)?

SOLUTION ATTEMPT
n
find_max_exp2(n):

    return ceil(log2(n+1))

binary = []
p = find_max_exp2(n)
for size in [2**exponent for exponent in range(p, -1)]:

    if n - size < 0:
        binary.append(0)
    else:
        binary.append(0)
        n-=size

THIS WAS NOT THE QEUSTOIN THAT WAS ASKED!!!

back to the question:we can try to answer

the answer is easy, start with [0, 0, 0, 0, 0…] and remember the sum=0, for each increment

conversions = {}
or start with [1, 1, 1, 1, … 1], sum=8, n=256.

    if sum < 0:
        return
    conversions[n] = sum


    for i in range(8):
        recurse(n-2**i, sum -1)


return [conversions[i] for i in range(n)]
"""