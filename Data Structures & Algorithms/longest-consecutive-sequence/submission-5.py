class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        good_nums = []
        for num in s:
            if num - 1 not in s:
                good_nums.append(num)

        if len(good_nums) == 0:
            return 0

        old_count = 1
        count = 0
        for num in good_nums:
            count = max(count, old_count)
            old_count = 1
            while num + 1 in s:
                old_count += 1
                num += 1
        return max(count, old_count)
