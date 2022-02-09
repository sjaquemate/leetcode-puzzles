"""

71. CLOSED (1) Longest Repeating Character Replacement - LeetCode

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.


Constraints:

- `1 <= s.length <= 10``5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

Let us think… we can store all in a dciontary char =’a’, [0, 1, 5] and their sorted indices, but then there are O(num_chars ncr k) strings to check
[0, 1, 2, 3, 5, 6, 7, 10]

doing something for each character is O(26)→ O(1)
look at ohw many
computer all interuptions: i.e ]4,], [8, 9]
[F]+[T, T, T, T, T, F, F, T, F]  find biggest with 2 F allowed:
queue(length=2) with their indices, such that you can recalculate when was the longest
qu = queue([-1], length=k+1)
for i in range(len(s)):

    if s[i] != ‘A’:
        qu.append_left(i)
    cur_len = qu[0] - qu[-1]
    max_len = max(max_len, cur_len),


This algoruithm is O(26*N) and O(N/26) space O(N) space worst case
"""