'''You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        a='z'
        q=0
        for i in letters:
            if i>target and i<=a:
                    a=i
                    q+=1
        if q==0:
            return letters[0]
        return a
obj=Solution()
print(obj.nextGreatestLetter(["c","f","j"], "a"))