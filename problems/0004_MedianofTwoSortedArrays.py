class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n=len(nums1)
        m=len(nums2)
        i=0
        j=0
        m1=0
        m2=0

        for k in range(0,(m+n)//2+1):
            m2=m1
            if i<n and j<m:
                if nums1[i]>nums2[j]:
                    m1=nums2[j]
                    j+=1
                else:
                    m1=nums1[i]
                    i+=1
                
            elif i<n:
                m1=nums1[i]
                i+=1

            elif j<m:
                m1=nums2[j]
                j+=1

        if(n+m)%2==1:
            return float(m1)
        else:
            return (float(m2)+float(m1))/2.0