


# nums = list(map(int, input().split(',')))

# nums.sort()
# s = 0
# e = len(nums) - 1
# result = []

# while s < e-1:
#     i = s + 1
#     while i < e:
#         if nums[s] + nums[i] + nums[e] == 0:
#             result.append((nums[s], nums[i], nums[e]))
#             e -= 1
#         elif nums[s] + nums[i] + nums[e] < 0:
#             i += 1
#         elif nums[s] + nums[i] + nums[e] > 0:
#             e -= 1
#     s += 1
#     e = len(nums) - 1
# result = list(set(result))

# final_result = []
# for i in result:
#     final_result.append(list(i))


# print(final_result)