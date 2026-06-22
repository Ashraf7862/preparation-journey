'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        r=""
        l=len(strs[0])
        q=len(strs)-1
        for i in range(l):
            if strs[0][i]==strs[q][i]:
                r+=strs[0][i]
            else:
                return r
        return r
obj=Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))