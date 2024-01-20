class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1

        while i < j:
            while i < len(s) and s[i].isalnum() == False:
                i += 1
            while j > -1 and s[j].isalnum() == False:
                j -= 1
            if i < len(s) and j > -1:
                if s[i].lower() != s[j].lower():
                    return False
            i += 1
            j -= 1

        return True

s = ".,"
obj = Solution()
print(obj.isPalindrome(s))