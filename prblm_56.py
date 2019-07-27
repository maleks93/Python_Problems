# https://leetcode.com/problems/merge-intervals/description/

# Time complexity: O( N*log(N) )
# Space complexity: O( N )

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        temp = self.sort(intervals) # sort the intervals with elements left element i.e. ele[0]
        
        #intervals.sort(key = lambda x : x[0])
        #temp = intervals
        
        result = [] # final result
        ind = 0
        
        while(ind <= len(temp)-1): # iterate over sorted intervals
            
            
            if len(result) > 0 and result[-1][1] >= temp[ind][0]: # if overlapping with last element in result
                result.append([result[-1][0],max(temp[ind][1], result[-1][1])])
                result.pop(-2)
                ind += 1
            elif ind == len(temp)-1: # final element
                result.append(temp[ind])
                break
            elif temp[ind][1] >= temp[ind+1][0]: # overlapping adjacent elements
                result.append([temp[ind][0],max(temp[ind][1], temp[ind+1][1])])
                ind += 2
            else: # non overlapping element
                result.append(temp[ind])
                ind += 1
                
        
        return result
    
    def sort(self, arr): # sort function to sort by 0th index of an element i.e. ele[0]
        
        if arr == None: # merge sort
            return None
        
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        
        left_sort = self.sort(arr[:mid])
        right_sort = self.sort(arr[mid:])
        
        ind_left = 0
        ind_right = 0
        result = []
        
        while(ind_left < len(left_sort) and ind_right < len(right_sort)):    
            if (left_sort[ind_left][0] < right_sort[ind_right][0]):
                result.append(left_sort[ind_left])
                ind_left += 1
            else:
                result.append(right_sort[ind_right])
                ind_right += 1
        
        if ind_left < len(left_sort):
            result += left_sort[ind_left:]
        
        if ind_right < len(right_sort):
            result += right_sort[ind_right:]
            
        return result
            
            
