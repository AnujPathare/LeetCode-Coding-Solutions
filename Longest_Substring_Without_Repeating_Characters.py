class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        tracker = 0
        record = {}
        max_sub_str = 0
        sub_str = 0

        for r in range(len(s)):
            if s[r] not in record:
                record[s[r]] = [0, r]
            record[s[r]][0] += 1
            
            if record[s[r]][0] == 1:
                sub_str += 1
                record[s[r]][1] = r
                if sub_str > max_sub_str:
                    max_sub_str = sub_str
                continue
            else:
                
                l = record[s[r]][1] + 1
                while tracker < l:
                    record[s[tracker]][0] -= 1
                    tracker += 1
                sub_str = r-l+1
                record[s[r]][1] = r
        return max_sub_str
    
obj = Solution()
s = "bprkpqlbtqpqphr"
print(obj.lengthOfLongestSubstring(s))