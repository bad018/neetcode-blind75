class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        last = {}
        l = 0
        for r, ch in enumerate(s):
            if ch in last and last[ch] >= l:
                l = last[ch] + 1
            last[ch] = r
            length = max(length, r - l + 1)
        return length

