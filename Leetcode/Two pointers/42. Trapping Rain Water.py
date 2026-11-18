'''
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''

class Solution:
    def trap(self, nums) -> int:
        n=len(nums)
        i=0
        j=n-1
        rmax=lmax=water=0
        while i<j:
            if nums[i]<nums[j]:
                rmax=max(rmax,nums[i])
                water+=(rmax-nums[i])
                i+=1
            else:
                lmax=max(lmax,nums[j])
                water+=(lmax-nums[j])
                j-=1
        return water

object=Solution()
print(object.trap([0,1,0,2,1,0,1,3,2,1,2,1]))