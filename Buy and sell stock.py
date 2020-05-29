#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# dp problem searches to the right of price[i] for the lowest buy price
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=float('infinity')
        for i in range(len(prices)):
            if buy>prices[i]:
                buy=prices[i]
            profit=max(profit,prices[i]-buy)    
        return profit

