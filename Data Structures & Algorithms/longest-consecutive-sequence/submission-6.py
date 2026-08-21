class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)

        if len(s) == 0:
            return 0
        for num in nums:
            s.add(num)

        counter = 0
        ans = 0
        while len(s) > 0:
            counter += 1
            base = next(iter(s))
            curr = base
            while curr - 1 in s:
                counter += 1
                curr -= 1
                s.discard(curr)

            s.discard(base)

            while base + 1 in s:
                counter += 1
                base += 1
                s.discard(base)
            
            ans = max(ans, counter)
            counter = 0

        return ans