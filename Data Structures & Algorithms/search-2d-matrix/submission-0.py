class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])

        top, bottom = 0, m - 1


        while top <= bottom:
            mid_row = (top + bottom) // 2

            row = matrix[mid_row]

            first = row[0]
            last = row[-1]

            if target > last:
                top = mid_row + 1
            elif target < first:
                bottom = mid_row-1
            else:
                l, r = 0, n - 1
                while l <= r:
                    mid = (l+r)//2
                    if row[mid] == target:
                        return True

                    elif row[mid] < target:
                        l = mid +1
                    else:
                        r = mid -1
                return False


        return False
