
# Quick Sort

# Avg Time complexity: O( NlogN )
# Worst case time complexity: O ( N^2 )

# Space complexity: O(1)

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        self.quick_sort(nums, 0, len(nums) - 1)
        return nums
    
    def partition(self, nums, low, hi):
        pivot_index = self.get_pivot(nums, low, hi)
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[low] = nums[low], nums[pivot_index]
        border = low
        
        for i in range(low, hi+1):
            if nums[i] < pivot_value:
                border += 1
                nums[border], nums[i] = nums[i], nums[border]
        nums[border], nums[low] = nums[low], nums[border]
        
        return border
        
    def quick_sort(self, nums, low, hi):
        
        if low < hi:
            p = self.partition(nums, low, hi)
            self.quick_sort(nums, low, p-1)
            self.quick_sort(nums, p+1, hi)
            
    def get_pivot(self, nums, low, hi):
        mid = (low + hi) // 2
        pivot = hi
        
        if nums[low] < nums[mid] < nums[hi]:
            pivot = mid
        elif nums[hi] > nums[low] > nums[mid]:
            pivot = low
        return pivot
