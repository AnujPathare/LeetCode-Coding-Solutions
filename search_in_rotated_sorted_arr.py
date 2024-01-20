class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[end]:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            
        return -1



# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
        
#         def binarySearch(start, end, target):
            
#             while start <= end:
#                 mid = (start + end) // 2
#                 if nums[mid] == target:
#                     return mid
#                 elif nums[mid] > target:
#                     end = mid - 1
#                 elif nums[mid] < target:
#                     start = mid + 1

#             return -1

#         def pivot(start, end):
            
#             start = 0
#             end = len(nums) - 1

#             while start < end:
                
#                 mid = (start + end) // 2
#                 if nums[mid] < nums[end]:
#                     end = mid
#                 else:
#                     start = mid + 1
            
#             return start
        

#         start = 0
#         end = len(nums) - 1
#         min_index = pivot(start, end)

#         right = binarySearch(min_index, end, target)
#         left = binarySearch(start, min_index-1, target)

#         if right == -1 and left == -1:
#             return -1
#         elif right != -1:
#             return right
#         else:
#             return left
    
nums = [4,5,6,7,0,1,2]
target = 0
obj = Solution()
print(obj.search(nums,target))