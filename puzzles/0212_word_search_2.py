"""

48. OPEN Word Search II - LeetCode

Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:

![](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)

    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]

Example 2:

![](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)

    Input: board = [["a","b"],["c","d"]], words = ["abcb"]
    Output: []


Constraints:

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 12`
- `board[i][j]` is a lowercase English letter.
- `1 <= words.length <= 3 * 10``4`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- All the strings of `words` are unique.

remaining = set(["oath","pea","eat","rain"])
letters = {‘a’: and their indices}
def step(i, j, seen=set(), intermediate=[], ):
letters = {(i, j): ‘a’} etc.
Node((i, j), char=’a’)
nodes = {(i,j): Node, defaultdict = None}
for i,j in range(i, j)

    nodes[(i, j)] = Node(i,j)

for i,j in range(i,j):

    nodes[(i,j)].right = nodes[(i, j-1)] etc

etc.
Node def get_next_nodes:

    return left, up, right, down

def step(node, seen=set(), word_queues):

    if node in seen:  # O(1)
        return
    seen.add(node)

if we have some same structure for our words…
"""