'''Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l=len(nums)
        c=[]
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    a=nums[i]+nums[j]+nums[k]
                    c.append(a)
        r=c[0]
        for i in range(1,len(c)):
            if abs(c[i]-target) < abs(r-target):
                r=c[i]
        return r
obj=Solution()
print(obj.threeSumClosest([-1,2,1,-4],1))