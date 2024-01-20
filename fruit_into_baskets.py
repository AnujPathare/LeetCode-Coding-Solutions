The below code is not accurate, try test case:
    [0,1,1,4,3]

# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
        
#         record = {}
#         l = 0
#         max_fruits = 0
#         for r in range(len(fruits)):
            
#             if fruits[r] not in record:
#                 record[fruits[r]] = 0
#             record[fruits[r]] += 1

#             if len(record) > 2:

#                 if last_index == 0:
#                     del record[fruits[last_index]]
#                 else:
#                     del record[fruits[last_index-1]]
#                 l = last_index
                
#             window = r-l+1
#             max_fruits = max(max_fruits, window)

#             if r < len(fruits)-1 and fruits[r+1] != fruits[r]:    
#                 last_index = r

#         return max_fruits