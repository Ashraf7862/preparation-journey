'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
'''

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        f=0
        for i in range(len(nums)):
            if nums[i]==target:
                f=1
                return i
        if f==0:
            for i in range(len(nums)):
                if target<nums[i]:
                    return i 
                elif i==len(nums)-1:
                    return i+1
obj=Solution()
print(obj.searchInsert([1,3,5,6],5))
