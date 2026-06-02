class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])

        l = 0
        r = len(matrix)-1
        m = int(r/2)

        row = m

        while l < r:
            print(l, m ,r)
            if matrix[m][0] == target or matrix[m][cols-1] == target:
                return True

            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][cols-1] < target:
                l = m + 1
            else:
                row = m
                break
            
            m = int((l+r)/2)

            row = m

        print("r ", row)
        l = 0
        if matrix[row][0] == target or matrix[row][cols-1] == target:
            return True
        r = cols-1
        m = int(r/2)

        while l < r:
            print(l, m, r)
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True

            m = int((r+l)/2)


        return False

            
