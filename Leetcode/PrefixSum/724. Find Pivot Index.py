'''Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
'''

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        p1=[nums[0]]
        p2=[0]*n
        p2[-1]=nums[-1]
        for i in range(1,n):
            p1.append(nums[i]+p1[i-1])
        for i in range(n-2,-1,-1):
            p2[i]=(nums[i]+p2[i+1])
        for i in range(n):
            if p1[i]==p2[i]:
                return i
        return -1

object=Solution()
print(object.pivotIndex([1,7,3,6,5,6]))