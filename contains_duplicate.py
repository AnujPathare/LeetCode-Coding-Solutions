lst = list(map(int, input().split(sep=',')))

def containsDuplicate(nums) -> bool:
    
    return len(set(nums)) != len(nums)
    
    # nums.sort()

    # for i in range(len(nums)-1):
    #     if nums[i+1] == nums[i]:
    #         return True
    
    # return False

    # record = {}

    # for i in nums:
    #     if str(i) not in record.keys():
    #         record[str(i)] = 1
    #     elif str(i) in record.keys():
    #         return True

    # return False

print(containsDuplicate(lst))