class Solution:
    def groupAnagrams(self, strs):

        # ------ O(n) time complexity ------ #

        dict1={}
        for word in strs:
            sorted_word= "".join(sorted(word))
            if sorted_word in dict1:
                dict1[sorted_word].append(word)
            else:
                dict1[sorted_word]= [word]
            break
        print(dict1)

        return(list(dict1.values()))

        # ------ O(n) time complexity ------ #

        # record = {}
        # index = 0

        # result = []
        # for word in strs:
        #     # print(''.join(sorted(word)))
        #     if (''.join(sorted(word))) in record:
        #         idx = record[''.join(sorted(word))]
        #         result[idx].append(word)
        #     else:
        #         result.append([word])
        #         record[(''.join(sorted(word)))] = index
        #         index += 1
        
        # print(f"result: {result}, \n record: {record}")


        # ------ O(n^2) time complexity ------ #

        # result = []

        # if len(strs) == 1:
        #     result.append(strs)
        #     return result


        # while strs != []:
        #     maintainer = []
        #     temp = ['']


        #     for i in range(1, len(strs)):
        #         if sorted(strs[0]) == sorted(strs[i]):
        #             temp.append(strs[i])
        #         else:
        #             maintainer.append(strs[i])
            
        #     temp[0] = strs[0]
        #     result.append(temp)
            
        #     strs = maintainer.copy()


        # return result

strs = ["eat","tea","tan","ate","nat","bat"]
obj = Solution()
print(obj.groupAnagrams(strs))