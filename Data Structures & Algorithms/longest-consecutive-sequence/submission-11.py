class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) == 0:
            k_longest = 0
        else: 
            k_longest = 1
        for num in nums:
            if num - 1 not in nums: # start of sequence
                n = num
                k = 1
                while (n + 1 in nums):
                    n += 1
                    k += 1
                    k_longest = max(k, k_longest) 

        return k_longest
 