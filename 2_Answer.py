def find_small_larg_no(arr):
    Min = []
    Max = []
    for i in range(len(arr)):
        if i % 2 == 0:
            Max.append(arr[i])
            
        elif i % 2 != 0:
            Min.append(arr[i])
            
    Min.sort()
    Max.sort()
    return sum([Min[1],Max[-2]])
    

num = list(map(int,input().split()))
if len(num) > 3:
    result = find_small_larg_no(num)
else:
    print('0')
print(result)
