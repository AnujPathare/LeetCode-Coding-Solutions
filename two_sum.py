# -------- O(n) complexity -------- #

class Solution:
    def twoSum(self, nums, target: int):

        record = {}

        for index, value in enumerate(nums):
            
            rem = target - value

            if rem in record:
                return [record[rem], index]
            else:
                record[value] = index

# -------- O(nlogn) complexity -------- #

# class Solution:
#     def twoSum(self, nums, target: int):

#         sorted_list = sorted(nums)

#         i = 0
#         j = len(nums) - 1

#         pair = [0,0]
        
#         while i < j:

#             if sorted_list[i] + sorted_list[j] == target:
#                 pair[0] = sorted_list[i]
#                 pair[1] = sorted_list[j]
#                 break
#             elif sorted_list[i] + sorted_list[j] > target:
#                 j -= 1
#             else:
#                 i += 1
        
#         indexes = []
#         for i in range(len(nums)):
#             if nums[i] == pair[0]:
#                 indexes.append(i)
#                 pair[0] = 9.99
#             elif nums[i] == pair[1]:
#                 indexes.append(i)
#                 pair[1] = 9.99
#             else:
#                 continue

#         return indexes
    
# nums = [2,7,11,15]
# target = 9
# nums = [6,6]
# target = 12
nums = [10,2,7,8,3,14]
target = 11

obj = Solution()
print(obj.twoSum(nums, target))