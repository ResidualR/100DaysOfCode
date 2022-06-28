class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    
        new_array = []
        left_pointer = 0
        right_pointer = len(nums)-1
        while left_pointer <= right_pointer:

            if pow(nums[left_pointer],2) >= pow(nums[right_pointer],2):
                new_array.append(nums[left_pointer]**2)
                left_pointer += 1
            else:
                new_array.append(nums[right_pointer]**2)
                right_pointer -= 1
        return new_array[::-1]