class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # left,right = -1,-1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         left = i
        #         break
        
        # for j in range(len(nums)-1,-1,-1):
        #     if nums[j] == target:
        #         right = j
        #         break
        
        # return [left,right]

        firstOccur,lastOccur = -1,-1
        first,last = 0,len(nums) - 1

        while first<=last:
            mid = (first+last)//2
            if nums[mid] == target:
                firstOccur = mid
                last = mid-1
            elif nums[mid] > target:
                last = mid-1
            else:
                first = mid+1

        first,last = 0,len(nums) - 1
        while first<=last:
            mid = (first+last)//2
            if nums[mid] == target:
                lastOccur = mid
                first = mid+1
            elif nums[mid] > target:
                last = mid-1
            else:
                first = mid+1

        return [firstOccur,lastOccur]