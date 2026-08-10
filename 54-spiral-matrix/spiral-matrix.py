class Solution(object):
    def spiralOrder(self, matrix):
        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1
        result = []
        while left <= right and top <= bottom:
            # left --> right
            for j in range(left,right + 1):
                result.append(matrix[top][j])
            top += 1

            # top ---> bottom 
            for i in range(top,bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # right ----> left
            if top <= bottom:
                for j in range(right,left-1,-1):
                    result.append(matrix[bottom][j])

                bottom -= 1

            # 4. Bottom → Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

            