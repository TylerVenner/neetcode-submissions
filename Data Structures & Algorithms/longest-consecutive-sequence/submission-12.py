class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) == 0:
            return 0
        else:
            k_longest = 0

        while (len(nums) > 0):
            n = nums.pop()
            curr_k = 1
            first_num = n
            while (n - 1 in nums):
                nums.remove(n - 1)
                n -= 1
                curr_k += 1

            n = first_num
            while (n + 1 in nums):
                nums.remove(n + 1)
                n += 1
                curr_k += 1

            k_longest = max(curr_k, k_longest)

        return k_longest

