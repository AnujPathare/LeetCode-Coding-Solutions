from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        counts = Counter(nums)
        print(counts)
        
        sorted_counts = sorted(counts.items(), key = lambda x: counts[1], reverse = True)
        print(sorted_counts)
        
        for key, val in counts.items():
            print(f"key: {key}, value: {val}")
        # for num, _ in sorted_counts:
            # print(num, _)

        # ---- O(nlogn) Time Complexity ---- #

        # record = {}

        # for elem in nums:
        #     if elem in record:
        #         record[elem] += 1
        #     else:
        #         record[elem] = 1

        # sorted_keys = sorted(record.keys(), key = lambda x: record[x], reverse = True)

        # result = []
        # for i in range(k):
        #     result.append(sorted_keys[i])

        # return result
    
nums = [3,7,4,1,2,3,7,1,2,1,7,3,3,7,7]
k = 2

obj = Solution()
print(obj.topKFrequent(nums, k))