'''You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.

 

Example 1:

Input: s = "abc"

Output: "abc"

Explanation:

There is no digit in the string.'''

class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in s:
            if i.isdigit():
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

object=Solution()
print(object.clearDigits('abc'))
