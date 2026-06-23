'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for z in range(len(nums)):
            nums[z]=nums[z]**2
        l=[0]*len(nums)
        m=nums.index(min(nums))
        i=m-1
        j=m
        k=0
        while i>=0 and j<len(nums):
            if nums[i]<=nums[j]:
                l[k]=nums[i]
                i-=1
            else:
                l[k]=nums[j]
                j+=1
            k+=1
        while i>=0:
            l[k]=nums[i]
            i-=1
            k+=1
        while j<len(nums):
            l[k]=nums[j]
            j+=1
            k+=1
        return l
obj=Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))