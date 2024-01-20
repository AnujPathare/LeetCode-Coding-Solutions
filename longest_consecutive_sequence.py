from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        record = defaultdict(list)
        unique = defaultdict(bool)
        max_seq_len = 0

        for num in nums:
            if unique[num]:
                continue

            unique[num] = True
            right, left = num, num
            
            if record[num + 1]:
                right = record[num + 1][1]
            if record[num - 1]:
                left = record[num - 1][0]
            
            record[right], record[left] = [left, right], [left, right]
            max_seq_len = max(max_seq_len, right-left+1)

        return max_seq_len

        # ------ O(nlogn) Time Complexity ------ #

        # nums = list(set(nums))
        # nums.sort()
        # # print(nums)

        # consecutive = 1
        # max = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1] + 1:
        #         consecutive += 1
        #         if i < len(nums)-1 and nums[i+1] != nums[i] + 1:
        #             if consecutive > max:
        #                 max = consecutive
        #             consecutive = 1
                    
        # if consecutive > max:
        #     max = consecutive
        
        # return max
    
nums = [100,4,200,1,3,2,5]
# nums = [3,2,5,4,3,6,2]
obj = Solution()
print(obj.longestConsecutive(nums))