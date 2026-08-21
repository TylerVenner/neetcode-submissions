class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        sorted_nums = sorted(nums)

        counter = 1
        ans = 1
        for i in range(len(nums)):
            if i == 0 or sorted_nums[i] == sorted_nums[i - 1]:
                continue
            elif sorted_nums[i] == sorted_nums[i - 1] + 1:
                counter += 1
            else:
                counter = 1

            ans = max(ans, counter)
        return ans