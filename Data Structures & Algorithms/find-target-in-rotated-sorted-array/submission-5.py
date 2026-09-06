class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        if j - i == 0 and nums[i] == target:
            return i


        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[i] == target:
                return i
            elif nums[j] == target:
                return j
            elif nums[j] > nums[mid] and (nums[j] > target and target > nums[mid]):
                i = mid + 1
            elif nums[j] > nums[mid]:
                j = mid - 1
            elif (target > nums[i] and target < nums[mid]):
                j = mid - 1
            else:
                i = mid + 1


        return -1
