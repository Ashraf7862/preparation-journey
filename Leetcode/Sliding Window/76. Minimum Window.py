'''76. Minimum Window Substring
Solved
Hard
Topics
premium lock icon
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        d={}
        for i in t:
            d[i]=d.setdefault(i,0)+1
        r=len(set(t))
        found=False
        k=0
        p={}
        m=float('inf')
        left=right=-1
        for i in range(n):
            if s[i] in d:
                p[s[i]]=p.setdefault(s[i],0)+1
                if not found:
                    found=True
                    j=i
                if p[s[i]]==d[s[i]]:
                    k+=1
            while k==r:
                if s[j] in p:
                    p[s[j]]-=1
                    if p[s[j]]<d[s[j]]:
                        k-=1
                    if i-j+1<m:
                        m=i-j+1
                        left=j
                        right=i
                j+=1
        if left!=-1:
            return s[left:right+1]
        return ""

object = Solution()
s1 = "ADOBECODEBANC"
t1 = "ABC"
s2 = "a"
t2 = "a"
s3 = "a"
t3 = "aa"
print(object.minWindow(s1, t1))  # Output: "BANC"
print(object.minWindow(s2, t2))  # Output: "a"  
print(object.minWindow(s3, t3))  # Output: ""