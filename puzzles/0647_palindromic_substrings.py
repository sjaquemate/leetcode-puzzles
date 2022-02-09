"""

75. CLOSED(1) Palindromic Substrings - LeetCode

Given a string `s`, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:

    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Constraints:

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

SOLUTION ATTEMP : Doable in N^2

for start in range(len(s))

    for j in range(len(s)):
        …
    if we create a dictionary in order
    bcbc
    ä”: [0]….

from inside to out:

N^2:

palindromes = []
add_palindromic(string, begin, end):

    if begin < 0 or end > n-1:
        reteurn
    if string[begin] != string[end]:
        return


    palindromes.append(string[begin:end])
    add_palindromic(string, begin-1, end+1)

for i in range(len(s)):

        add_palindromic(string, i, i)  # for odd palindromes
        if i > 0:
            add_palindromic(string, i, i-1)  # for even palindromes
"""