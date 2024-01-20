class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        left = 0
        sub_arr = 0
        min_len = 100001

        for right in range(len(nums)):
            sub_arr += nums[right]

            while sub_arr >= target:
                min_len = min(min_len, right - left + 1)
                sub_arr -= nums[left]
                left += 1
        
        return 0 if min_len == 100001 else min_len