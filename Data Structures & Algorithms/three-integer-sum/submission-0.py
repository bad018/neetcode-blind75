class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)):
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] == target:
                    ans.add(tuple([nums[i],nums[j],nums[k]]))
                    j += 1
                    k -= 1
                    
        return list(ans)

