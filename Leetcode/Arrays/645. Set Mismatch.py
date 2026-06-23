'''You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]'''

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        r=len(nums)
        c=[]
        for i in nums:
            if nums.count(i)>1:
                c.append(i)
                break
        q=[]
        for i in range(1,r+1):
            q.append(i)
        for i in q:
            if i not in nums:
                c.append(i)
        return c
obj=Solution()
print(obj.findErrorNums([1,2,2,4]))
