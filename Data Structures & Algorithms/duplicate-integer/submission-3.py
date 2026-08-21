class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for k in nums:
            s.add(k)

        return len(s) != len(nums)