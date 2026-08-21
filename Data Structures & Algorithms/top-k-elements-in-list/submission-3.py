class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}

        for n in nums:
            d1[n] = d1.get(n, 0) + 1

        t = [[] for i in range(len(nums) + 1)]

        for n, count in d1.items():
            t[count].append(n)

        ans = []

        for i in range(len(t) - 1, 0, -1):
            for n in t[i]:
                ans.append(n)

            if len(ans) == k:
                return ans