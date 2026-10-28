'''Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        if a==a[::-1]:
            return True
        else:
            return False
object=Solution()
print(object.isPalindrome(121))