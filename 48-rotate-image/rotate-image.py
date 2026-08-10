import numpy as np 
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i +1 , n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(len(matrix[0])):
            left = 0
            right = len(matrix)-1
            while left < right:
                matrix[i][left],matrix[i][right] = matrix[i][right],matrix[i][left]
                left += 1
                right -=1

        return matrix
        
        