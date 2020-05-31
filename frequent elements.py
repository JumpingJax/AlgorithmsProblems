#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        print(d)
        final=[]
        sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
        print(sorted_d)
        res=dict(list(sorted_d.items())[0:k])
        print(res)
        for i in res:
            final .append(i)
        return final

