# nums = list(map(int, input().split()))
nums = [2,2,7,5,4,3,2,2,1]

def nextPermutation(nums: list[int]) -> None:

    if list(reversed(sorted(nums))) == nums:
        nums.reverse()
        print(nums)
        return

    desc = 0
    for i in range(len(nums)-1):
        if nums[i+1] > nums[i]:
            desc = i+1
    

    start = desc
    end = len(nums)-1
    while start < end:

        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1



    for i in range(desc, len(nums)):
        if nums[i] > nums[desc-1]:
            temp = nums[i]
            nums[i] = nums[desc-1]
            nums[desc-1] = temp
            break
    
    print(nums)


nextPermutation(nums)