class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, m*n - 1


        while i <= j:
            mid = (i+j)//2
            col = mid%n
            row = (mid-col)//n

            if matrix[row][col] == target: 
                return True
            elif matrix[row][col] < target:
                i = mid + 1
            else :
                j = mid - 1
        
        return False