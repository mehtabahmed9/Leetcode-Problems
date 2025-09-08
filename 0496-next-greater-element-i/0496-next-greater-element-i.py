class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # result = []
        # for num in nums1:
        #     index = nums2.index(num)
        #     print('index-->',index)
        #     nge = -1

        #     for j in range(index+1,len(nums2)):
        #         if nums2[j] > num:
        #             nge = nums2[j]
        #             break
        #     result.append(nge)
        # return result

        stack = []
        dic = {}
        result = []

        for num in reversed(nums2):
            while stack and stack[-1]<num:
                stack.pop()
            
            #stack is empty
            if not stack:
                dic[num] = -1

            #current element is greater than current num
            else:
                dic[num] = stack[-1]
            stack.append(num)

        for i in range(len(nums1)):
            result.append(dic[nums1[i]])
        return result