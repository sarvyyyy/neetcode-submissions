class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = m*n
        left = 0
        right = l-1
        while left<=right:
            mid = (left+right) // 2
            ind1 = mid // n
            ind2 = mid % n
            elem = matrix[ind1][ind2]
            if elem == target:
                return True
            elif elem > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
