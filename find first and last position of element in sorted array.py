#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # start and end index of the target
        start, end = -1, -1
        n = len(nums) -1
        low = 0
        high = n
        
        # when its empty list return [-1, -1]
        if not nums:
            return [start, end]
        
        # Only 1 element in nums
        if high == 0:
            if nums[high] == target:
                return [0, 0]
            else:
                return [start, end]

        # We must first find the start index of the target. Since nums is sorted list
        # we can keep narrowing our search by comparing target > nums[mid].
        # In this list [5,7,7,8,8,10] we are searching for start index of 8.
        while low < high:
            mid = (low + high) //2
            # if number is lesser than target, move search to right half
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        # At the end of this cycle, we are left with starting index of the target.
        # If it not equal to target, target was not found in the nums.
        # We must stop our search.
        if nums[low] != target:
            return [start, end]
        else:
            start = low
            
        # Since we found starting index, we do another search starting from 
        # next element [8,10] i.e. we do not need to search in [5,7,7,8] any more.
        low = start + 1
        high = n
        
        while low < high:
            mid = (low + high) //2
            # every time number is equal to index, we must move to right
            if nums[mid] == target:
                low = mid + 1
            else:
                high = mid
        
        # Now we can end up with index of the target or index of element that
        # follows the end index of target.
        if nums[high] != target:
            # since the index != target, our end index is previous element.
            end = high - 1
        else:
            end = high
        
        return [start, end]

