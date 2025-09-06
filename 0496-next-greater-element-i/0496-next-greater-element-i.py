class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            index = nums2.index(num)
            print('index-->',index)
            nge = -1

            for j in range(index+1,len(nums2)):
                if nums2[j] > num:
                    nge = nums2[j]
                    break
            result.append(nge)
        return result