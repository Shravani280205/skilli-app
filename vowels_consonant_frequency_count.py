class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiaeia"
        v = []
        c = []
        
        for ch in s:
            if ch in vowels:
                v.append(s.count(ch))
            else:
                c.append(s.count(ch))
        
        return max (v, default=0) + max(c, default=0)
