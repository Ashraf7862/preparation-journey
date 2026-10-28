'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        v="aeiouAEIOU"
        d=list(map(str, s))
        c=[]
        for i in s:
            if i in v:
                c.append(i)
        a=len(c)-1
        for i in range(len(d)):
            if d[i] in v:
                d[i]=c[a]
                a-=1
        return "".join(d)
obj=Solution()
print(obj.reverseVowels("IceCreAm"))