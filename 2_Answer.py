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



def Productsmallpair(arr,smm):
    if len(arr) < 2:
        return -1
    else:
        arr.sort()
        i = 1
        while i < len(arr):
            if (arr[i-1] + arr[i]) < smm:
                return (arr[i-1] * arr[i])
            i += 1
                
smm = int(input())
num = list(map(int,input().split()))

result = Productsmallpair(num, smm)
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







N = int(input())
num = int(input())
rem = 0 
ans = ''
while num != 0:
    rem = num % N
    if rem >= 9:
        ans += chr(55+rem)
    else:
        ans += str(rem)
    num = num // N
    
print(ans[::-1])


