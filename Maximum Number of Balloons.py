#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic={}
        for i in text:
            dic[i]=0
        for i in text:
            dic[i]+=1
        
        if 'b' in text and 'a' in text and 'l' in text and 'o' in text and 'n' in text:
        #for key,value in dic.items():
            dic['l']=dic['l']//2
            dic['o']=dic['o']//2
            return min(dic['b'],dic['a'],dic['l'],dic['l'],dic['o'],dic['o'],dic['n'])
        return 0

