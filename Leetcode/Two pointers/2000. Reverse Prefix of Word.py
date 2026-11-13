'''Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

 

Example 1:

Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".'''

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        lst=list(word)
        j=-1
        n=len(word)
        for i in range(n):
            if word[i]==ch:
                j=i
                break
        if j==-1:
            return word
        i=0
        while i<j:
            lst[i],lst[j]=lst[j],lst[i]
            i+=1
            j-=1
        return "".join(lst)

object=Solution()
print(object.reversePrefix("abcdefd","d"))
