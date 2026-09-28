class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) -1
        l = 0

        for k in range(len(matrix)-1, -1, -1):
            if matrix[k][i] <= target:
                l = k
                break


        while i <= j:
            m = (i+j)//2
            if matrix[l][m] < target:
                i = m+1
            elif matrix[l][m] > target:
                j = m-1
            else:
                return True
        
        return False