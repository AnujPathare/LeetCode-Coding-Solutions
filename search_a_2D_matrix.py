class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        def binarySearch(nums,target):

            start = 0
            end = len(nums) - 1

            while start <= end:

                mid = (start + end) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
            
            return False

        start = 0
        end = len(matrix) - 1
        result = False

        while start <= end:

            mid = (start + end) // 2

            if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid])-1]:
                result = binarySearch(matrix[mid],target)
                return result
            elif target > matrix[mid][len(matrix[mid])-1]:
                start = mid + 1
            elif target < matrix[mid][0]:
                end = mid - 1

        return False



matrix = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]
target = 61
obj = Solution()
print(obj.searchMatrix(matrix, target))


# class Solution:
#     def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
#         def binarySearch(l,r,num_pos,nums,target):

#             start = 0
#             end = len(nums) - 1

#             if nums[start] <= target <= nums[end]:

#                 while start <= end:

#                     mid = (start + end) // 2
#                     if nums[mid] == target:
#                         return True, True
#                     elif nums[mid] < target:
#                         start = mid + 1
#                     elif nums[mid] > target:
#                         end = mid - 1

#                 l = 1
#                 r = -1
#                 return l,r
            
#             elif target < nums[start]:
#                 r = num_pos - 1
#                 return l,r
#             elif target > nums[end]:
#                 l = num_pos + 1
#                 return l,r

#         l = 0
#         r = len(matrix) - 1
#         mid_pos = r-l // 2

#         while 0 <= mid_pos <= len(matrix)-1:

#             if mid_pos == True:
#                 return True
#             if mid_pos == -1:
#                 return False
#             else:
#                 l,r = binarySearch(l,r,mid_pos,matrix[mid_pos],target)
#                 if l == True:
#                     return True
#                 elif l == r:
#                     l,r = binarySearch(l,r,mid_pos,matrix[mid_pos],target)
#                 mid_pos = r-l // 2
        



# matrix = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]
# target = 4
# obj = Solution()
# print(obj.searchMatrix(matrix, target))