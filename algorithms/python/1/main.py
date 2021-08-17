class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            if target - n in nums[i + 1:]:
                return [i, nums[i + 1:].index(target - n) + (i + 1)]

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        nums_map = collections.defaultdict(int)
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return i, nums_map[target - num]