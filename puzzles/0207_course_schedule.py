"""


45. OPEN Course Schedule - LeetCode

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a``i``, b``i``]` indicates that you must take course `b``i` first if you want to take course `a``i`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

Example 1:

    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0. So it is possible.

Example 2:

    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Constraints:

- `1 <= numCourses <= 10``5`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= a``i``, b``i` `< numCourses`
- All the pairs prerequisites[i] are unique.

prerequisites[i].length == 2, and all pairs prerequisites[i] are unique

SOLUTION ATTEMPT
courses may be linked, i.e: [5, 6], [6, 8].
From a prerequisite we can do a requisite. if we start randomly (O(N)) and continue randomly if allowed (O(N-1) … our solution is O(N!). however, we can also try to match / chain prerequisites, like so:

8 → 6 → 5, which will turn into some kind of tree structure. To make this tree it takes O(N^2) if we do it naively, then then the question becomes: how many courses can we take? Take None as root, we just count the number of nodes, since there are no duplicates in the tree. This is O(N). Now to then create the tree efficiently is the real task. ( Node: value=course_nr, children= List[Node] ) We know a prereq is always higher up in the tree. If we know the first prereq and link it like: None → Node(value=prereq_first), and keep a dictionary to that Node, we can find and link the rest efficiently as well (O(1) per operation)…. Now how to find an unlinked course without reqs?, for sure this will be found in all rights

 Also node this tree can NOT contain circles… there should be a test for that as well… validate_tree_endings… (this can be done using a dictionary and recursion)

 root = Node(value=None, children=[]).

 Otherwise, we can also just start out somewhere at the beginning and start linking if the course node does not exist yet, e.g:
 [5, 6], [7, 4] [6, 7],
 6 → 5 → []

 4 → 7 → []
 So something like:

 tree_heads = []
 nodes = {}
 for (course, preqreq) in preqrequirements:


     if course not in nodes:
        nodes[course] = Node(value=course, children=[])
    if preqreq not in nodes:
        nodes[prereq] = Node(value=preqreq, children=[])


    # these pairs are unique, so this is valid:
    nodes[preqreq].addChild(nodes[course])
    nodes[course].addParent(nodes[prereq])

seen = set()
tree_starts = []

get_tree_start(node):

    if node in seen:
        return
    seen.add(node)

    if len(node.parents) == 0:
        tree_starts.append(node)
    else:
        for parent in node.parents:
            get_root(parent)

def get_tree_starts():  # those that do not have parents

    for _, node in nodes.items():
        get_tree_start(node)

Now from all tree_starts we continue, but we have to wait if a child node has multiple parents . In effect, we are actually searching for how many courses we actaully CAN do… but whatever…, that also solves our question:

To really answer this question we also have to check for inner-loops/consistency, so the question is left open for now…
"""