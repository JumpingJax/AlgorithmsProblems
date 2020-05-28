#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        if N==1 or N==2:
            return 1
        dp=[-1]*N
        dp[1]=1
        dp[0]=1
        
        for i in range(2,N):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[N-1]
        


# In[ ]:




