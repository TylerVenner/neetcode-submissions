class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        h = {}

        for i, k in enumerate(nums):
            h[k] = i

        for i, k in enumerate(nums):
            diff = target - k
            if diff in h and h[diff] != i:
                return [i, h[diff]]
