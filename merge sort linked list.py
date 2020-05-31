#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        def getmid(node):
            if not node:
                return node
            cur=node
            prev=node
            while cur.next and cur.next.next:
                prev=prev.next
                cur=cur.next.next
            return prev
        def mergesort(node):
            if not node or not node.next:
                return node
            mid=getmid(node)
            nextmid=mid.next
            mid.next=None
            left=mergesort(node)
            right=mergesort(nextmid)
            sortedlist=sortedMerge(left,right)
            return sortedlist
            
        def sortedMerge(a, b): 
            result = None
          
            # Base cases 
            if a == None: 
                return b 
            if b == None: 
                return a 
              
        # pick either a or b and recur.. 
            if a.val <= b.val: 
                result = a 
                result.next =sortedMerge(a.next, b) 
            else: 
                result = b 
                result.next =sortedMerge(a, b.next) 
            return result 
            
        return mergesort(head)

