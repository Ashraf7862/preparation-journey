'''You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r'''

class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        c=""
        i=0
        j=0
        while i<len(a) and j<len(b):
            c+=a[i]
            c+=b[j]
            i+=1
            j+=1
        while i<len(a):
            c+=a[i]
            i+=1
        while j<len(b):
            c+=b[j]
            j+=1
        return c
obj=Solution()
print(obj.mergeAlternately("abc", "pqr"))
