'''You are given an array of positive integers nums.

An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

prod(arr) is the product of all elements of arr.
gcd(arr) is the GCD of all elements of arr.
lcm(arr) is the LCM of all elements of arr.
Return the length of the longest product equivalent subarray of nums.

 

Example 1:

Input: nums = [1,2,1,2,1,1,1]

Output: 5

Explanation: 

The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

'''
import math

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        m=0
        for i in range(n):
            p=1
            l=1
            g=0
            for j in range(i,n):
                p*=nums[j]
                l=math.lcm(l,nums[j])
                g=math.gcd(g,nums[j])
                if p==l*g:
                    m=max(m,j-i+1)
        return m


object=Solution()
print(object.maxLength([1,2,1,2,1,1,1]))