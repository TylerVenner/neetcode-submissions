class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums) - 2):
            table = {}
            target = -1 * nums[i]
            for j in range(i + 1, len(nums)):
                diff = target - nums[j]
                if diff in table:
                    triplet = tuple(sorted([nums[i], nums[j], diff]))
                    ans.add(triplet)
                else:
                    table[nums[j]] = j

        return [list(triplet) for triplet in ans]
