"""


23. OPEN Word Search - LeetCode

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

Example 2:

![](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true

Example 3:

![](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false


Constraints:

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.


Follow up: Could you use search pruning to make your solution faster with a larger `board`?

board[i,j] size mxn, word[k] size w.

SOLUTION ATTEMPT:
if we just start somewhere and find the first letter of word, then go either left or down to

place all relevant letters in a dictionary of size worstcase mxn, start at first letter word, start a search for next letter of word in the 2 expected places and continue like that until last letter.
One problem here is that we cannot have any intermediate [a, b, c, d]. Example, with a bad space space complexity O(MxN):

target = “target”
letters = defaultdict([])
for i in range(N):

    for j in range(M):
        s = matrix[i, j]
        letters[s].append((i, j))

# for t in target:
we will try all solutions in order:
for t in
def traverse(…, intermediate = [], …)


    next_letter = letters[t]

"""