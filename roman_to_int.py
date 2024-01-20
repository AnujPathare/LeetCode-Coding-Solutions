s = input("Enter roman number:\n")

roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
number=0
for i in range(len(s)-1):
    if roman[s[i]] < roman[s[(i+1)]]:
        number-=roman[s[i]]
    else:
        number+=roman[s[i]]

print(number+roman[s[-1]])



#----------------------------------------------------------------------#


# s = input("Enter roman number:\n")

# roman_to_integer = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000,
#         }
# s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
# print(sum(map(lambda x: roman_to_integer[x], s)))
# # print(list(map(lambda x: roman_to_integer[x], s))


#----------------------------------------------------------------------#


# s = input("Enter Roman number:\n")

# thousand = ''
# hundred = ''
# tens = ''
# units = ''
# count = 0
# for i in range(len(s)):
    
#     if s[i] == 'M' and count == 0:
#         thousand += s[i]
#         continue
    
#     if s[i] in ['C', 'D', 'M']:
#         count = 1
#         if i > 0 and s[i] == 'C' and s[i-1] == 'X':
#             tens += s[i]
#             continue
#         hundred += s[i]
#         continue
    
#     if s[i] in ['X', 'L', 'C']:
#         if i > 0 and s[i] == 'X' and s[i-1] == 'I':
#             units += s[i]
#             continue
#         tens += s[i]
#         continue
    
#     units += s[i]



# result = 0

# for q in range(len(thousand)):
#     result += 1000

# for q in range(len(hundred)):
#     if q == 1 and hundred[q].lower() == 'd':
#         result += 300
#         continue
#     elif q == 1 and hundred[q].lower() == 'm':
#         result += 800
#         continue

#     if hundred[q].lower() =='c':
#         result += 100
#     elif hundred[q].lower() =='d':
#         result += 500    


# for q in range(len(tens)):
#     if q == 1 and tens[q].lower() == 'l':
#         result += 30
#         continue
#     elif q == 1 and tens[q].lower() == 'c':
#         result += 80
#         continue

#     if tens[q].lower() =='x':
#         result += 10
#     elif tens[q].lower() =='l':
#         result += 50    


# for q in range(len(units)):
#     if q == 1 and units[q].lower() == 'v':
#         result += 3
#         continue
#     elif q == 1 and units[q].lower() == 'x':
#         result += 8
#         continue

#     if units[q].lower() =='i':
#         result += 1
#     elif units[q].lower() =='v':
#         result += 5  

# print(f'thousand: {thousand} \nhundred: {hundred} \ntens: {tens} \nunits: {units} result: {result}')