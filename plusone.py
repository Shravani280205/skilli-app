from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for d in digits:
            s = s + str(d)
        num = int(s) + 1
        ans = []
        for ch in str(num):
            ans.append(int(ch))
        return ans