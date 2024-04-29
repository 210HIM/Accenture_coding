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







def check_eqval(s1,s2):
    s1 = s1.upper()
    s2 = s2.upper()
    for i in s1:
        if i in s2:
            return 'Yes'
        else:
            return 'No'


#input()
str_1 = input()
str_2 = input()
print(check_eqval(str_1,str_2))
