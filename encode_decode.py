class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here

        enc = ""
        for i in strs:
            temp = str(len(i)) + ':' + i
            enc += temp

        return enc

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here

        i = 0
        dec = []
        while i < len(str):
            
            word = ""
            num = int(str[i])
            i += 2
            for _ in range(num):
                word += str[i]
                i += 1
            dec.append(word)
        
        return dec


# class Solution:
#     """
#     @param: strs: a list of strings
#     @return: encodes a list of strings to a single string.
#     """
#     def encode(self, strs):
#         # write your code here

#         enc = "Z^#.".join(strs)
#         return enc

#     """
#     @param: str: A string
#     @return: decodes a single string to a list of strings
#     """
#     def decode(self, str):
#         # write your code here

#         dec = str.split("Z^#.")
#         return dec
    
lst = ["we", "say", ":", "yes"]
obj = Solution()
enc = obj.encode(lst)
dec = obj.decode(enc)
print(enc)
print(dec)