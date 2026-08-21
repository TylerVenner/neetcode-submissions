class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 1, len(numbers)
        while left < right:
            curr_sum = numbers[left - 1] + numbers[right - 1]
            if curr_sum == target:
                return [left, right]
            elif curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
