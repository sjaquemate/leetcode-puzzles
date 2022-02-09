"""

76. CLOSED(1) Longest Common Subsequence - LeetCode

Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

    Input: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

    Input: text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.


Constraints:

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

SOLUTION ATTEMPT
daddy, ddy
d [0, 2, 3] | [0, 1]
a [1]  | []
y [4] | [2]

Facts is subseqeuence has to begin and end somewhere on both texts
Create a matrix of

    d a d d y

  d T    T T
  d T    T T
  y              T

 d (0,0), d(0,2), d(0,3)
 d (1,0), d(1, 2), d(1,3)
 y (2, 4)

 max_paths = {((0, 0): max_len=0, (0,2): max_len=0} etc
 max_len = 0
 def recurse(i=0,  j=len(text1), cur_length):

     if i > len(text2) or j >len(text1):
        return

     if (i,j) in max_paths:
         max_paths[(i,j)] += cur_path
         recurse(i+1, j+1, cur_length)
     e;se:
        recurse(i,j+1,cur_length)

 …Something along these lines


 This algorithm is O(N^2) time and o(N^2)worst case
"""