class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        l, r = 0, n*m

        while l < r:
            mid = (r+l) // 2
            col = mid%m
            row = (mid-col)//m


            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid
            else: 
                l = mid + 1

        return False
