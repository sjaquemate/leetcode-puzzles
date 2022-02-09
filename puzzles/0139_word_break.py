"""


35. CLOSED Word Break - LeetCode

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
    Note that you are allowed to reuse a dictionary word.

Example 3:

    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false


Constraints:

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are unique.

SOLUTION ATTEMPT:
edge example:
appleapples, [apple, apples]
 one iteration: if “leet” in “leetcode”: remove one leet and continue. we need to try all attempts so for now I don’t see anything quickers, use python’s find method “Python String find() method returns the lowest index of the substring if it is found in a given string. If it is not found then it returns -1. “ Now, we only need ONE true

 can_segment(string, words):

     if len(string) == 0:
        return True
    if not any(word in string for word in words):  # nothing fits anymore
        return False


    for word in words:  # traverse all words that fit (guaranteed at least more than 1)
        result = string.find(word)
        result != -1:
            start, end = result, result+len(word)
            if can_segment(string[start:end]):
                return True

    return False

"""