'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c=0
        a=len(s)
        for i in range(len(t)):
            if c<a:
                if s[c]==t[i]:
                    c+=1
        if c==a:
            return True
        return False
obj=Solution()
print(obj.isSubsequence("abc", "ahbgdc"))