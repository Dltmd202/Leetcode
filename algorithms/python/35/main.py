class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        ans = (left + right) // 2
        while left < right:
            ans = (left + right) // 2
            if nums[ans] == target:
                return ans
            elif nums[ans] < target:
                left = ans + 1
            elif nums[ans] > target:
                right = ans - 1
        return left + 1 if nums[left] < target else left