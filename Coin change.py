#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp=[amount+1]*(amount+1)
        dp[0]=0
        # calculating minimum number of coins to make ith cent
        for i in range(amount+1):
            # iterate over coins if coins[j]<=i we try it
            # we then check if the current amount of coins is less than 1 cus we took one coin + dp[i-coins[j]]
            # so i cents minus however many cents we just took
            # we see the min value we can create and see if that is in the array coins
            for j in range(len(coins)):
                if coins[j]<=i:
                    dp[i]=min(dp[i],1 + dp[i - coins[j] ])
                # if coins[j] is bigger than i we break since theres no point searching for even bigger coins in a sorted array
                else:
                    break
        if dp[amount]<=amount:
            return dp[amount]
        return -1

