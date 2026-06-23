'''Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.'''

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n=len(arr)
        arr.sort()
        a=float('inf')
        c=[]
        for i in range(1,n):
            d=arr[i]-arr[i-1]
            if d<a:
                c=[]
                a=d
            if d==a:
                c.append([arr[i-1],arr[i]])
        return c
obj=Solution()
print(obj.minimumAbsDifference([4,2,1,3]))
