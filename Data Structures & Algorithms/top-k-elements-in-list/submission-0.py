from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        sorted_dict = sorted(d.items(),key=lambda x: x[1], reverse=True)
        return [num for num, freq in sorted_dict[:k]]