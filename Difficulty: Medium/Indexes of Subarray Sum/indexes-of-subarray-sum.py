#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        left = 0
        current_sum = 0
        
        for right in range(len(arr)):
            # Expand the window by adding the current element
            current_sum += arr[right]
            
            # Shrink the window from the left if the sum exceeds target
            while current_sum > target and left < right:
                current_sum -= arr[left]
                left += 1
                
            # Check if the current window sum matches the target
            if current_sum == target:
                # Returning 1-based indices as per standard competitive programming requirements
                return [left + 1, right + 1]
                
        return [-1]