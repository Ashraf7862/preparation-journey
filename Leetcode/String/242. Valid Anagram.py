'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=sorted(list(s))
        b=sorted(list(t))
        if a==b:
            return True
        return False
object=Solution()
print(object.isAnagram("anagram", "nagaram"))