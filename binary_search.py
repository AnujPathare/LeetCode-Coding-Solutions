def binarySearch(nums, target):

# ------ Binary Search for a list sorted in ascending order with duplicate elements ------ #
    
    # nums.sort()

    start = 0
    end = len(nums)-1
    
    while start <= end:
        
        mid = (start + end) // 2
        if nums[mid] == target:

            # ---- More Optimal ---- #

            if mid == 0 or nums[mid-1] != nums[mid]:
                return mid
            else:
                end = mid-1

            # ---- Less Optimal ---- #

            # if mid == 0:
            #     return mid
            # else:
            #     while nums[mid-1] == nums[mid]:
            #         mid -= 1
            #         if mid == 0:
            #             return 0
            # return mid
            
        elif nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
    
    not_found = "Target not found."
    return not_found

# ------ Binary Search for a list sorted in ascending order with unique elements ------ #

# def binarySearch(nums, target):
    

#     start = 0
#     end = len(nums)-1
    
#     while start <= end:
        
#         mid = (start + end) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             end = mid - 1
#         elif nums[mid] < target:
#             start = mid + 1
    
#     not_found = "Target not found."
#     return not_found
        

# nums = [5,7,2,3,8,1]
# nums = [1,2,3,5,7,8]
nums = [1, 3, 3, 3, 3, 3, 3, 3]
target = 3
print(f"Index of {target} is: {binarySearch(nums, target)}")
