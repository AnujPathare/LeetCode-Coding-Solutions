n = int(input())
result = []

for i in range(1, n+1):
    temp = []
    for j in range(i):

        if j == 0 or j == i-1:
            temp.append(1)

        else:
            temp.append(result[i-2][j-1] + result[i-2][j])
    
    result.append(temp)

print(result)