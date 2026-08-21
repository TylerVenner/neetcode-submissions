class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i, n in enumerate(nums):
            h[n] = i

        for i in range(len(nums)):
            need = target - nums[i]

            if need in h and i != h[need]:
                return [min(i, h[need]), max(i, h[need])]
