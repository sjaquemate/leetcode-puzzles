"""


3. OPEN Longest Palindromic Substring - LeetCode

Given a string `s`, return the longest palindromic substring in `s`.

When is a string palindromic?
if s[0] = s[-1], etc:

def is_palindromic(substring):

    if len(substring) <= 1:  # base case
        return True
    if substring[0] != substring[-1]:  # escape case
        return False
    is_palindromic(substring[1:-1])

O(w), w: size of word.  IDEA start from the end towards the beginning of the word

input: string
output: string(start_index:start_index+max_len)

two cases:
"baaab"
“abba”
“acbc”
moving cases:
“abbaxyacaca”

def longest_palindromic_substring(s):

    max_len = 0
    end_index = None
    last_place = 0
    last_index = {}

    for i, s in enumerate(string):
        if s in last_index:
            diff = i - last_index[s]
            if diff % 2 == 0:  # even
                start_index = last_index[s]

        max_len = max(max_len, i - start_index+1)
        
        last_index[s] = i

"""