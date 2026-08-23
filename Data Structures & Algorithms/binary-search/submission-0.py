class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while (i <= j):
            n = nums[(j + i) // 2]

            if n == target:
                return (j + i) // 2
            elif n > target:
                j = (i + j) // 2 - 1
            elif n < target:
                i = (i + j) // 2 + 1

        return -1
