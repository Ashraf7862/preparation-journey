'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        l=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                l[i][j]=matrix[n-j-1][i]
        matrix[:]=[row for row in l]
obj=Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj.rotate(matrix)