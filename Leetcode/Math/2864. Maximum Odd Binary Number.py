'''You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.

 

Example 1:

Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".'''

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        r=sorted(s,reverse=True)
        n=len(s)
        for i in range(n):
            if r[i]=='0':
                r[i-1],r[-1]=r[-1],r[i-1]
                break
        return "".join(r)

object=Solution()
print(object.maximumOddBinaryNumber("010"))