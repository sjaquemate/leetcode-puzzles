"""

65. CLOSED (1) Coin Change - LeetCode

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.
You may assume that you have an infinite number of each kind of coin.

Example 1:

    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

Example 2:

    Input: coins = [2], amount = 3
    Output: -1

Example 3:

    Input: coins = [1], amount = 0
    Output: 0


Constraints:

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2``31` `- 1`
- `0 <= amount <= 10``4`

just like the adding ones and twos, we can solve this using recursion, lets not optimize for recursion per se

min_coins_spent = float(‘inf’)
coins = sorted(coins, ascending=False)  # sort descending

coin_change(coins, target, coins_spent=0):

    if coins_spent > min_coins_spent:
        return
    if target == 0:
        min_coins_spent = min(min_coins_spent, coins_spent)
    if target <= 0:
        return

    for coin in coins:
        coin_change(coins, target-coin, coins_spent+=1)

if min_coins_spent == float(‘inf’)

    return -1

return min_coins_spent


This works, but grows exponentially O(num_coins^target). I don’t think there is a faster way, we would need to solve
n * x1 + n * x2 = target, using % we can only do if we have i.e. [2, 1]=coins etc.
"""