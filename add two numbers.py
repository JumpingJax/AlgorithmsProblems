#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val = 0
        next_val = False
        
        result = None
        next_result = None
        while l1 != None or l2 != None or next_val == True:
            if l1 != None:
                val += l1.val
                l1 = l1.next
            if l2 != None:
                val += l2.val
                l2 = l2.next
            if next_val:
                val += 1
                next_val = False
            if val > 9:
                next_val = True
                val -= 10
            if result != None:
                next_result.next = ListNode(val)
                next_result = next_result.next
            else:
                next_result = ListNode(val)
                result = next_result
            val = 0
        return result

