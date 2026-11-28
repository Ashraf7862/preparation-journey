'''Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

Example 1:


Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.'''


import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head):
        temp = head

        while temp.next != None:
            res = math.gcd(temp.val, temp.next.val)

            new = ListNode(res)
            new.next = temp.next
            temp.next = new

            temp = new.next

        return head


head = ListNode(18)
head.next = ListNode(6)
head.next.next = ListNode(10)
head.next.next.next = ListNode(3)



object = Solution()


result = object.insertGreatestCommonDivisors(head)


temp = result

while temp:
    print(temp.val, end=" -> ")
    temp = temp.next

print("None")
