
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for n in nums:
            d[n] = d.get(n, 0) + 1

        l = [[] for _ in range(len(nums) + 1)]
        for n, count in d.items():
            l[count].append(n)

        ans = []
        for i in range(len(l) - 1, 0, -1):
            for n in l[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans