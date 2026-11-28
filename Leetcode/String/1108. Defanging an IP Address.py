'''Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
'''

class Solution:
    def defangIPaddr(self, address: str) -> str:
        res=""
        for i in address:
            if i=='.':
                res+='[.]'
            else:
                res+=i
        return res

object=Solution()
print(object.defangIPaddr("1.1.1.1"))