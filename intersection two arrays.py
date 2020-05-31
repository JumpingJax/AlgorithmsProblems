#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        liste=[]
        for i in nums1:
            if i in nums2 and i not in liste:
                liste.append(i)
                
        return liste
        

