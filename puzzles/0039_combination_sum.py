"""

11. CLOSED Combination Sum - LeetCode

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.
The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.


    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.


    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

cand_sorted = sorted(candidates)

[2, 3, 6, 7]
Note that we can check for duplicates by % operator.
First n1num1 + n2*num2  = total.
Take total/num1 = n1 + n2*num2/num1, this we can solve for n1 and n2 being integers
now:
total/num1 = n1 + n2num2/num1 + n3*num3/num1
AND
total/num3 = n3 + n2num2/num1 + n3*num3/num1 etc.
So this becomes a matrix

total/num1  =  [ 1           num2/num1] n1
total/num2  =    [ num1/num2           1] n2
i.e total = 5, num1 = 1, num2 = 2, only has one solution

5 = [1 2]
2.5 = [0.5, 1]

etc. In general this is O(N^3) to solve. But these are integers… so probably there is something faster… AND MORE IMPORTANTLY: this matrix will have an infinite amount of solutions, but we are only interested in the integer ones…;)
This is also called a linear Diophantine equation, where is allowed to be zero.

Nvm this idea
HINT:

![Combination Sum Leetcode Solution](https://www.tutorialcup.com/wp-content/uploads/2021/03/combination-sum.jpg?ezimgfmt=rs%3Adevice%2Frscb41-1)


GIVEN SOLUTION:

    def combinationSum(self, candidates, target):
            result = []
            self.combinationSumRecu(sorted(candidates), result, 0, [], target)
            return result

        def combinationSumRecu(self, candidates, result, start, intermediate, target):
            if target == 0:
                result.append(list(intermediate))
            while start < len(candidates) and candidates[start] <= target:
                intermediate.append(candidates[start])
                self.combinationSumRecu(candidates, result, start, intermediate, target - candidates[start])
                intermediate.pop()
                start += 1

result = []
sorted(candidates), result = result, intermediate = [], start=0, target=target
if target < 0:

    return

if target == 0:

    result.append(list(intermediate))
    return

while start < len(candidates) # for loop…, and candidates[start] <= target # to make sure current one is definitely over…

    intermediate.append(candidates[start])  # current one
    combinationsumrecu(candidates, result, start, intermediate, target - current
    intermediate.pop() # remove the one that will be coming from one level down again
    start ++

IMO this is more easily rewritten in a for loop, like so:

candidates = sorted(candidates)
result = []
intermediate = []
start = 0
TARGET
combination_sum(start, TARGET)
combination_sum(start, target):

    if target == 0:
        result.append(intermediate)
        return
    if target < 0:
        return


    while start < len(candidates):
        candidate = candidates[start]
        intermediate.append(candidate)
        combination_sum(start, target - candidate)
        intermediate.pop()  # backtracking ;)
        start += 1

time complexity will be O(N^M), M biggest sublist, worstcase N^N
"""