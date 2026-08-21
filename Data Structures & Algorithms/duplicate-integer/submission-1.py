class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashset = set()
        
        for k in nums:
            hashset.add(k)

        return len(hashset) != len(nums)
