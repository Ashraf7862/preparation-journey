'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2=sorted(set(nums2))
        l=len(nums1)-1
        c=[]
        for r in nums2:
            k=0
            j=l
            while k<=j:
                mid=(k+j)//2
                if nums1[mid]==r:
                    c.append(r)
                    break    
                elif nums1[mid]<r:
                    k=mid+1
                else:
                    j=mid-1
        return c

obj=Solution()
print(obj.intersection([1,2,2,1],[2,2]))