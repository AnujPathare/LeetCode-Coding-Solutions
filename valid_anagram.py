class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if len(s) != len(t):
        #     return False
        
        # TLE, bad logic

        # for i in range(len(s)):               
        #     if sorted(s)[i] != sorted(t)[i]:
        #         return False
            
        return True
    
s = ''
t = ''

obj = Solution()
print(obj.isAnagram(s, t))