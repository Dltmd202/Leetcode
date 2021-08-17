class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            init = nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                if init + nums[left] + nums[right] == 0:
                    res.add((init, nums[left], nums[right]))
                if init + nums[left] + nums[right] > 0:
                    right -= 1
                elif init + nums[left] + nums[right] <= 0:
                    left += 1
        return list(res)