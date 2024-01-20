class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        max_storage = 0
        i = 0
        j = len(height) - 1
        while i < j:
            min_height = min(height[i], height[j])
            storage = (j-i) * min_height
            if storage > max_storage: max_storage = storage
            if height[i] == min_height:
                i += 1
            elif height[j] == min_height:
                j -= 1
            
        return max_storage
    
height = [1,1]
# height = [1,8,6,2,5,4,8,3,7]
obj = Solution()
print(obj.maxArea(height))