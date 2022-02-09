"""


30. CLOSED Best Time to Buy and Sell Stock - LeetCode

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i``th` day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

SOLUTION ATTEMPT:
We can calculate the differences per day: [0, -6, 4, -2, 3, -2] and take the cumulative sum:
[0, -6, -2, -4, -1, -3] Now the highest point and the lowest point will tell it all, however, we must make sure that the lowest point is BEFORE the highest point… if that's not the case, there simply was never an opportunity to buy and sell for a profit, because prices were only decreasing…
edge case example:
[10, 0, 5, -5]
[0, -10, 5, -10]
[0, -10, -5, -15]

another example
[10, 20, 30, 0, 100]
[0, 10, 10, -30, 100]
[0, 10, 20, -10, 90]
result thus is
optimal_buy_sell(prices):

    diff = [0] + [right-left for left, right in zip(prices[:-1], prices[1:])]
    runningsum = cumsum(diff)
    high= max(runningsum[1:])  # you can never buy the first day;)
    low = min(runningsum[:arghigh])

O(N) algorithm

"""