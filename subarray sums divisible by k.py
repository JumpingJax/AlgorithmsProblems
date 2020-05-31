#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
	def subarraysDivByK(self, A: List[int], K: int) -> int:
		d = {0:1}
		s = 0
		res = 0
		for i in A:
			s += i
			s %= K
			if s == 0:
				res += d[0]
			elif s in d:
				res += d[s]
			if s not in d:
				d[s] = 1
			else:
				d[s] += 1
		return res

