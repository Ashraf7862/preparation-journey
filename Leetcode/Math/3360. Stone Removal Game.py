'''Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.

Alice starts by removing exactly 10 stones on her first turn.
For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
The player who cannot make a move loses the game.

Given a positive integer n, return true if Alice wins the game and false otherwise.

 

Example 1:

Input: n = 12

Output: true

Explanation:

Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
Bob cannot remove 9 stones, so Alice wins.'''

class Solution:
    def canAliceWin(self, n: int) -> bool:
        i=10
        turn=1
        while n>=0:
            n-=i
            i-=1
            turn=1 if turn==0 else 0
        return True if turn else False

object=Solution()
print(object.canAliceWin(12))
