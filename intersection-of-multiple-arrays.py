nums = [[7,34,45,10,12,27,13],[27,21,45,10,12,13]]

res = []
concat = []

for i in range(len(nums)):
    concat += nums[i]

for i in set(concat):
    if concat.count(i) == len(nums):
        res.append(i)
print(sorted(res))


# mini = 1001
# smallest = [[]]

# for i in nums:
#     if len(i) < mini:
#         smallest[0] = i
#         mini = len(i)

# smallest = smallest[0]
# nums.sort(key=len)

# result = []
# for i in nums:
#     print(i)
#     for j in smallest:
#         if j not in i:
#             result.append(j)

# final = [x for x in smallest if x not in result]
# final.sort()
# print(f"Common integers: {final}")