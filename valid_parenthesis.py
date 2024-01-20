# class Solution: # Higher time complexity than below
#     def isValid(self, s: str) -> bool:
#         while '()' in s or '[]' in s or '{}' in s:
#             s = s.replace('()', '').replace('[]', '').replace('{}', '')
#             print(s)
#         return True if len(s) == 0 else False
   
# obj = Solution()
# obj.isValid('({[]})')

# class Solution:
#     def isValid(self, s: str) -> bool:
        
#         stack = []

#         for char in s:
#             if char in '({[':
#                 stack.append(char)
#             else:
#                 if stack and ((char == ']' and stack[-1] != '[') or (char == '}' and stack[-1] != '{') or (char == ')' and stack[-1] != '(')):
#                     return False
#                 else:
#                     if stack:
#                         stack.pop()
#                         continue
#                     else:
#                         return False
    
#         return not stack