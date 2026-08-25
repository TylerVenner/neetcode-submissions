class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        i, j = 0, len(matrix) - 1
        row = -1
        while j >= i:
            mid = (i + j) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                j = mid - 1
            else:
                # first check if space to search up 
                # then see if current mid is the FIRST below target
                # by checking the one above
                if mid + 1 > j or matrix[mid + 1][0] > target:
                    row = mid
                    break
                # else, just continue binary search
                else:
                    i = mid + 1

        if row == -1:
            return False

        i, j = 0, len(matrix[0]) - 1
        while j >= i:
            mid = (i + j) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return False
