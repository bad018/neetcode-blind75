from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = defaultdict(int)
        for ch in s:
            seen[ch] += 1
        for ch in t:
            seen[ch] -= 1
            if seen[ch] < 0:
                return False
        return True
