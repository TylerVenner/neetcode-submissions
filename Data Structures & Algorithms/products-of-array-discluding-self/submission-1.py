class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        
        left = []
        for i in range(size):
            if i == 0:
                left.append(nums[i])
            else:
                left.append(nums[i] * left[i - 1])
        
        right = []
        for i in range(size):
            if i == 0:
                right.append(nums[size - i - 1])
            else:
                right.append(nums[size - i - 1] * right[i - 1])

        ans = []
        for i in range(size):
            if i != 0 and i != size - 1:
                ans.append(left[i - 1] * right[size - i - 2])
            elif i == 0:
                ans.append(right[size - 2])
            elif i == size - 1:
                ans.append(left[size - 2])

        return ans