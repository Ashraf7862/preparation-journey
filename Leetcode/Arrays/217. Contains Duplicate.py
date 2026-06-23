'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        a=0
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                a=1
                break
        if a==0:
            return False
        else:
            return True
obj=Solution()
print(obj.containsDuplicate([1,2,3,1]))
