"""


42. CLOSED House Robber - LeetCode

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

Example 2:

    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.

It is not as simple as checken odd and even indicies. Now…, we can do the same as the the maximum subarray…. Using recursion and a dictionary this is easily solved:

seen = {}
nums = [2,7,9,3,1]
def rob_houses(index = 0, max_heist=0 cur_heist = 0):

    if index >= len(nums):
        return max_heist
    if index in seen:
        return seen[index]

    cur_heist += nums[index]
    max_heist = max(max_heist, cur_heist)
    heist_option1 = rob_houses(index+2 max_heist, cur_heist)
    heist_option2 = rob_houses(index+3, max_heist, cur_heist)
    seen[index] = max(heist_option1, heist_option2)

rob_houses(index=0)
rob_houses(index=1)
return max(seen[0], seen[1])

O(N) in time, O(N) in space… (if heist can be negative just skip it aka don’t take it. Maximal in time complexity (evaluates strategy from every house only once…) Probably not perfect in space complexity…

another fun try could be calculating the even cumsum and odd cumsum and picking the maximum by checking the max strategy, i.e: (this would still be O(N) in space
[2,7,9,3,1]
2, 2, 11, 11, 12
0, 7, 7, 10, 10… I don’t see a quick logical way to solve it like this…


This double recursion call will not be improved in this way… We can try to sort the houses?
However, this would be effectively an O(N^2) solution… The problem is that we are reevaluating the same places   Example:
[10, 5, 10, 100]
best: 110.
looking at max(nums) does not help, because:
[10, 90, 100, 90].

Say we look at three houses next to eachother [90, 100, 90], [50, 0, 30]. If

"""