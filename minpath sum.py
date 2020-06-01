#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        
        def recur(grid,i,j,dp):
            
            if dp[i][j]!=0:
                return dp[i][j]
            if i==len(grid)-1 and j==len(grid[0])-1:
                
                dp[i][j]=grid[i][j]
            
            if i==len(grid)-1 and  j!=len(grid[0])-1:
                
                dp[i][j]=grid[i][j]+recur(grid,i,j+1,dp)
                
                
            
            if i!=len(grid)-1 and j==len(grid[0])-1:
                
                dp[i][j]=grid[i][j]+recur(grid,i+1,j,dp)
                
                
            
            if i!=len(grid)-1 and j!= len(grid[0])-1:
                
                dp[i][j]=grid[i][j]+min(recur(grid,i+1,j,dp),recur(grid,i,j+1,dp))
                
            return dp[i][j]
            
            
            
        return recur(grid,0,0,dp)

