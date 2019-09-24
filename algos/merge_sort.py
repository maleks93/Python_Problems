
# Merge Sort

# Avg Time complexity: O( NlogN )
# Worst/Best case Time complexity: O( NlogN )

# Space complexity: O(N)

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Merge sort
        
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2
        
        left_sort = self.sortArray(nums[0:mid])
        right_sort = self.sortArray(nums[mid:])
        
        result = []
        
        left_ind = 0
        right_ind = 0
        
        while(left_ind < len(left_sort) and right_ind <len(right_sort)):
            if left_sort[left_ind] < right_sort[right_ind]:
                result.append(left_sort[left_ind])
                left_ind += 1
            else:
                result.append(right_sort[right_ind])
                right_ind += 1
        
        if left_ind < len(left_sort):
            result += left_sort[left_ind:]
        if right_ind <len(right_sort):
            result += right_sort[right_ind:]
            
        return result
