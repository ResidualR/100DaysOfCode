class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        upper = len(nums) - 1
        lower = 0

        while lower <= upper:
            
            mid = (upper+lower) // 2 
            print(mid)
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                
                lower = mid + 1 
                
            else:
                upper = mid - 1

        return lower