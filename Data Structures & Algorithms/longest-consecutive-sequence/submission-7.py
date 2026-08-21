class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        if len(s) == 0:
            return 0
        
        ans = 0
        while s:
            base = s.pop()
            length = 1

            # expand left
            curr = base - 1
            while curr in s:
                length += 1
                s.remove(curr)
                curr -= 1

            # expand right
            curr = base + 1
            while curr in s:
                length += 1
                s.remove(curr)
                curr += 1

            ans = max(ans, length)

        return ans