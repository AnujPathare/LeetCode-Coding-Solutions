class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        start = 0
        end = len(nums) -1

        while start < end:
            
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
            
        return nums[start]



# class Solution:
#     def findMin(self, nums:list[int]) -> int:
        
#         start = 0
#         end = len(nums) -1

#         if len(nums) == 1:
#             return nums[0]
#         while start <= end:
            
#             mid = (start + end) // 2

#             if nums[mid] > nums[mid+1]: # mid < len(nums) -1 and 
#                 return nums[mid+1]
            
#             elif nums[mid] > nums[end]:
#                 start = mid + 1
            
#             elif nums[mid] < nums[end]:
#                 end = mid
#                 if start == end:
#                     return nums[start]

        
# nums = [2,3,4,10,20,31]
# nums = [20,31,2,3,4,10]
nums = [3,4,10,20,31,2]
# nums = [2,3,4,10,20,31,1]
# nums = [1]

obj = Solution()
print(obj.findMin(nums))