class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        k, current = 1, nums[0]
        for i in range(1, len(nums)):
            if current != nums[i]:
                current = nums[i]
                nums[k] = current
                k += 1
        return k