class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        ans = 0
        d = {}

        for j in range(len(s)):
            if s[j] in d:
                i = max(i, d[s[j]] + 1)

            d[s[j]] = j
            ans = max(ans, j - i + 1)

        return ans
