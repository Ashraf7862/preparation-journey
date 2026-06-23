'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]'''

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        l=[]
        for i in range(1,n+1):
            l.append([1]*i)
        for i in range(n):
            for j in range(i):
                if j!=0 and j!=i:
                    l[i][j]=l[i-1][j-1]+l[i-1][j]
        return l
    
obj=Solution()
print(obj.generate(5))