'''You are given a string s and an integer k.

Reverse the first k characters of s and return the resulting string.

 

Example 1:

Input: s = "abcd", k = 2

Output: "bacd"

Explanation:​​​​​​​

The first k = 2 characters "ab" are reversed to "ba". The final resulting string is "bacd".'''

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        r=s[:k][::-1]
        return r+s[k:]

object=Solution()
print(object.reversePrefix("abcd",2))
