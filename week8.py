def canPartition(nums):
    total = sum(nums)
    # If the sum is odd, we can't split into two equal subsets
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(nums)
    dp = [False] * (target + 1)
    dp[0] = True  # base case: zero sum is always possible with no elements

    for num in nums:
        for i in range(target, num - 1, -1):  # iterate backwards
            dp[i] = dp[i] or dp[i - num]

    return dp[target]
def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # 0 coins needed for amount 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1
def maxSubArray(nums):
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum