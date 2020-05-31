#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = [""]
        for digit in digits:
            res = [word + letter for letter in phone[digit] for word in res]
        return res

