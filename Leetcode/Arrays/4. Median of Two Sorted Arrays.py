'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=len(nums1)
        b=len(nums2)
        k=a+b
        c=[0]*k
        d=0
        for i in range(a):
            c[d]=nums1[i]
            d+=1
        for i in range(b):
            c[d]=nums2[i]
            d+=1
        c.sort()
        if len(c)%2!=0:
            return c[k//2]
        else:
            l=k//2
            return (c[l]+c[l-1])/2
        
obj=Solution()
print(obj.findMedianSortedArrays([1,3],[2]))