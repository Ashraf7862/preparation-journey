'''Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

 

Example 1:

Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.'''

class Solution:
    def checkString(self, s: str) -> bool:
        q=0
        found=False
        n=len(s)
        for i in range(n):
            if s[i]=='a' and found:
                return False
            elif s[i]=='b':
                found=True
        return True

object=Solution()
print(object.checkString("aaabbb"))