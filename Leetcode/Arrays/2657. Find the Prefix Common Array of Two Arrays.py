'''You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

 

Example 1:

Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
'''

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        vis=set()
        n=len(A)
        res=[0]*n
        count=0
        for i in range(n):
            if A[i] in vis:
                count+=1
            vis.add(A[i])
            if B[i] in vis:
                count+=1
            vis.add(B[i])
            res[i]=count
        return res

object=Solution()
print(object.findThePrefixCommonArray([1,3,2,4],[3,1,2,4]))