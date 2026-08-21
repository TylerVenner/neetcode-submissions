class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in need:
                return [need[nums[i]], i]
            else:
                need[diff] = i

