'''Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=[]
        p=0
        for i in nums:
            if i==1:
                p+=1
                c.append(p)
            else:
                p=0
                c.append(p)
        return max(c)
obj=Solution()
print(obj.findMaxConsecutiveOnes([1,1,0,1,1,1]))