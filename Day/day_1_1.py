class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = 0
        
        
        while left<=right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            else:
                if target > nums[mid]:
                    left = mid+1
                elif target < nums[mid]:
                    right = mid-1
        return -1