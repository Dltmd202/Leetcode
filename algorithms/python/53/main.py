class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = [0]
        ans = nums[0]
        for i in range(len(nums)):
            left.append(left[-1] + nums[i])

        for i in range(len(nums)):
            ans = max(ans, left[i + 1] - min(left[:i + 1]))
        return ans