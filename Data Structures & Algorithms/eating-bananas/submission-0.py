class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = piles[0]
        for pile in piles:
            if pile > max_pile:
                max_pile = pile

        i, j = 1, max_pile
        while (i < j):
            k = (j + i) // 2
            running_total_hours = 0
            for pile in piles:
                running_total_hours += -(-pile // k)

            if running_total_hours > h:
                i = k + 1
            else:
                j = k

        return i
