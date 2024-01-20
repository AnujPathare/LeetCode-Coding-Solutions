class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        # ------ O(n) Time Complexity and assigning one list ------ #

        result = [1]
        mult = 1
        for i in range(1, len(nums)):
            mult *= nums[i-1]
            result.append(mult)

        print(result)

        mult = 1
        for i in range(-2, -len(nums)-1, -1):
            mult *= nums[i+1]
            result[i] *= mult

        return(result)

        # ------ O(n) Time Complexity but assigning 3 lists ------ #
        # pref_list = [1]
        # suff_list = [1]
        # mult = 1

        # zero_count = 0
        # if nums[0] == 0:
        #     zero_count = 1
        
        
        # for i in range(1,len(nums)):
        #     if nums[i] == 0:
        #         zero_count += 1

        #     mult *= nums[i-1]
        #     pref_list.append(mult)

        #     if zero_count > 1:
        #         return [0] * len(nums)
        
        # mult = 1
        # for i in range(-2, -len(nums)-1, -1):
        #     mult *= nums[i+1]
        #     suff_list = [mult] + suff_list

        # result = []
        # for i in range(len(nums)):
        #     result.append(pref_list[i] * suff_list[i])

        # return result

nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
obj = Solution()
print(obj.productExceptSelf(nums))