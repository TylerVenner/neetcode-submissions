class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if nums[i] in h:
                return [h[nums[i]], i]
            else:
                h[need] = i