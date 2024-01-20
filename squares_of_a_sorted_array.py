class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        result = []
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i]*nums[i] > nums[j]*nums[j]:
                result.append(nums[i]*nums[i])
                print(nums[i]*nums[i])
                i += 1
            elif nums[i]*nums[i] < nums[j]*nums[j]:
                result.append(nums[j]*nums[j])
                print(nums[j]*nums[j])
                j -= 1
            elif nums[i]*nums[i] == nums[j]*nums[j]:
                result.append(nums[i]*nums[i])
                result.append(nums[j]*nums[j])

                i += 1
                j -= 1

        if i == j:
            result.append(nums[i]*nums[i])

        return list(reversed(result))

nums = [-1,1]
obj = Solution()
print(obj.sortedSquares(nums))

# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:

        # if len(nums) == 1:
        #     return [nums[0]*nums[0]]
        # elif nums[-1] <= 0:
        #     return [nums[i]*nums[i] for i in range(-1, -len(nums)-1, -1)]
        
        # start = 0
        # end = len(nums) - 1
        # least_positive = 100001
        # least_positive_index = len(nums)+1

        # while start <= end:

        #     mid = (start + end) // 2
        #     if nums[mid] > 0 and nums[mid] < least_positive:
        #         least_positive = nums[mid]
        #         least_positive_index = mid
        #         end = mid - 1
        #     elif start == end and nums[start] == least_positive and start == 0 :
        #         break
        #     elif start == end and nums[start] == least_positive and (nums[start-1] == nums[start]):
        #         print("eexcccc")
        #         start -= 1
        #         end -= 1
        #         least_positive_index = start
        #     elif start == end and nums[start] == least_positive and (nums[start-1] < nums[start] and nums[start-1] < 0):
        #         least_positive_index = start
        #         break
        #     elif nums[mid] == 0:
        #         least_positive = nums[mid]
        #         least_positive_index = mid
        #         break
        #     elif nums[mid] < 0:
        #         start = mid + 1


        # neg_squares = []
        # for i in range(least_positive_index-1, -1, -1):
        #     neg_squares.append(nums[i]*nums[i])
        
        # pos_squares = []
        # for i in range(least_positive_index, len(nums)):
        #     pos_squares.append(nums[i]*nums[i])

        # print(neg_squares)
        # print(pos_squares)
        # result = []
        # i = 0
        # j = 0
        # while i < len(pos_squares) and j < len(neg_squares):
        #     if pos_squares[i] < neg_squares[j]:
        #         result.append(pos_squares[i])
        #         i += 1
        #     elif pos_squares[i] > neg_squares[j]:
        #         result.append(neg_squares[j])
        #         j += 1
        #     elif pos_squares[i] == neg_squares[j]:
        #         result.append(pos_squares[i])
        #         result.append(neg_squares[j])
        #         i += 1
        #         j += 1
        
        # if len(result) == len(nums):
        #     return result
        # elif i == len(pos_squares):
        #     if j < len(neg_squares):
        #         for index in range(j, len(neg_squares)):
        #             result.append(neg_squares[index])
        # elif j == len(neg_squares):
        #     if i < len(pos_squares):
        #         for index in range(i, len(pos_squares)):
        #             result.append(pos_squares[index])
        # return result


# nums = [-10,-6,-5,-3,-2,-2,3,3,3,5]
# obj = Solution()
# print(obj.sortedSquares(nums))