
def search(nums, target):
        
    init = 0
    last = len(nums)-1
    succ = False
    
    while init<=last and not False:
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

print(search([13, 11, 10, 7, 4, 3, 1, 0],7))