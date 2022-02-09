"""


56. CLOSED Valid Anagram - LeetCode

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:

    Input: s = "rat", t = "car"
    Output: false


Constraints:

- `1 <= s.length, t.length <= 5 * 10``4`
- `s` and `t` consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

SOLUTION ATTEMPT
make a dictionary of letters with a count: letter_count, then remove them again. check if all of them are zeros in the end:

def valid_anagram(s, t):

    letter_count = {default=int}


    for char in s: # add
        letter_count[char] += 1


    for char in t:  # remove
        letter_count[char] -= 1


    return all(count==0 for count in letter_count.values())

space and time complexity of O(len(s) + len(t))
"""