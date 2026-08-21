class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        
        for n in nums:
            h[n] = h.get(n, 0) + 1

        counter_indexed_list = [[] for i in range(len(nums) + 1)]

        for n, count in h.items():
            counter_indexed_list[count].append(n)

        ans = []
        for i in range(len(counter_indexed_list) - 1, 0, -1):
            for n in counter_indexed_list[i]:
                ans.append(n)

            if len(ans) == k: # can place here bc answer is unique
                return ans