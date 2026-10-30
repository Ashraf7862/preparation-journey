'''A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=set()
        for i in sentence:
            s.add(i)
        return True if len(s)==26 else False

object= Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(object.checkIfPangram(sentence))