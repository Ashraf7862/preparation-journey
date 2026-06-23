'''Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        c=[]
        for i in range(n-3):
            if i>0 and nums[i-1]==nums[i]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j-1]==nums[j]:
                    continue
                k=j+1
                z=n-1
                while k<z:
                    s=nums[i]+nums[j]+nums[k]+nums[z]
                    if s==target:
                        c.append([nums[i],nums[j],nums[k],nums[z]])
                        k+=1
                        z-=1
                        while k<z and nums[k-1]==nums[k]:
                            k+=1
                        while k<z and nums[z+1]==nums[z]:
                            z-=1
                    elif s<target:
                        k+=1
                        while k<z and nums[k-1]==nums[k]:
                            k+=1
                    else:
                        z-=1
                        while k<z and nums[z+1]==nums[z]:
                            z-=1
        return c
obj=Solution()
nums = [1,0,-1,0,-2,2]
