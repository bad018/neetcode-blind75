from collections import defaultdict, Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0
        max_len = 0
        for r, ch in enumerate(s):
            freq[ch] += 1
            max_freq = max(freq.values(), default=0)
            if r - l + 1 - max_freq > k:
              freq[s[l]] -= 1
              l += 1
            max_len = max(max_len, r - l + 1)
                
        return max_len

