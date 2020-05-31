#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list_1 = nums1 + nums2
        list_1.sort()
        len_sorted_array = len(list_1)
        if len_sorted_array % 2 == 0:
            median = (list_1[(len_sorted_array-1) // 2] + list_1[((len_sorted_array-1) // 2)+1]) / 2
        elif len_sorted_array % 2 != 0:
            median = list_1[(len_sorted_array-1) // 2]
        return median

