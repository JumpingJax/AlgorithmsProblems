#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        for i in arr:
            dic[i]=0
        for i in arr:
            dic[i]+=1
        newlist=[]
        for key,value in dic.items():
            if value in newlist:
                return False
            if value not in newlist:
                newlist.append(value)
            
        return True

