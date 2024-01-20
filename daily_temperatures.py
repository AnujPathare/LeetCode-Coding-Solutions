class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answer = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < temp:
                prev_temp_index = stack.pop()
                answer[prev_temp_index] = index - prev_temp_index
            stack.append(index)

        return answer


# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
#         result = []
#         for i, temp in enumerate(temperatures):
#             i += 1
#             count = 1
#             while i < len(temperatures):
                
#                 if temperatures[i] > temp:
#                     result.append(count)
#                     break
#                 i += 1
#                 count += 1
#             if i == len(temperatures):
#                 result.append(0)
#         return result

# obj = Solution()
# temperatures = [30, 60, 90]
# print(obj.dailyTemperatures(temperatures))