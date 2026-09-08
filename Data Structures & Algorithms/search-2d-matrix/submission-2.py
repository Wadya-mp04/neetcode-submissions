class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix) - 1
        target_row = -1
        while u <= d:
            mid = (u+d)//2
            if(matrix[mid][0] == target):
                return True
            elif(matrix[mid][0] < target):
                target_row = mid
                u = mid+1
            else:
                d = mid - 1
        
        if(target_row == -1):
            return False
        
        l, r = 0, len(matrix[target_row]) - 1
        while (l<=r):
            mid = (l+r)//2
            if(matrix[target_row][mid] == target):
                return True
            elif(matrix[target_row][mid]  > target ):
                r = mid - 1
            else:
                l = mid + 1
            
        return False
