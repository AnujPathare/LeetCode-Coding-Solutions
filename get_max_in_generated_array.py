n = int(input())

def lol(n):
        if n == 0:
            return 0

        elif n == 1:
            return 1

        else:
            result = [0,1]
            
            for i in range(n-1):
                    result.append(0)

            # print((n//2)+1)
            for i in range(1, (n//2)+1):

                    result[2 * i] = result[i]
                    if ((2 * i) + 1) <= n:
                        result[(2 * i) + 1] = result[i] + result[i + 1]

            return max(result)

    
print(lol(n))