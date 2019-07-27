# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Time complexity: O( N )
# Space complexity: O( 1 )

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = 0 # leftmost index
        r = len(numbers) - 1 # rightmost index
        
        while(l<r):
            
            if numbers[l]+numbers[r] == target: # if hot the target, return the indexes
                return [l+1 , r+1]
            elif numbers[l] + numbers[r] > target: # decr r if overshooted the target
                r -= 1
            elif numbers[l] + numbers[r] < target: # incr l if undershooted the target
                l += 1
