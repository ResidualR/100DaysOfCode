class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        init = 0
        last = len(nums)-1
        succ = False
    
        while init<=last and not succ:
            mid = (init+last)//2
            if nums[mid] == target:
                succ = True
                return mid
            else:
                if target<nums[mid]:
                    last = mid-1
                else:
                    init = mid+1
        return -1
