
# 3-way Quick sort

# Time complexity: O( NlogN )
# Space complexity: O(1)

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 3-way quick sort (Dutch National flag algo)
        
        self.three_way_quick_sort(nums, 0, len(nums)-1)
        
        return nums
        
    def three_way_quick_sort(self, nums, lo, hi):
        
        if (hi - lo) < 1:
            return
        
        i, j = self.partition(nums, lo, hi)
        
        self.three_way_quick_sort(nums, lo, i-1)
        self.three_way_quick_sort(nums, j+1, hi)
        
    def partition(self, nums, lo, hi):
        
        pivot_index = self.find_pivot(nums, lo, hi)
        pivot_value = nums[pivot_index]
        
        mid = lo
        
        while (mid <= hi):
            
            if nums[mid] < pivot_value:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                mid += 1
                lo += 1
            elif nums[mid] == pivot_value:
                mid += 1
            elif nums[mid] > pivot_value:
                nums[hi], nums[mid] = nums[mid], nums[hi]
                hi -= 1
        
        return lo, hi
    
    def find_pivot(self, nums, lo, hi):
        mid = (lo + hi) // 2
        
        pivot_index = hi
        
        if nums[lo] < nums[mid] < nums[hi]:
            pivot_index = mid
        elif nums[hi] > nums[lo] > nums[mid]:
            pivot_index = lo
            
        return pivot_index
    
