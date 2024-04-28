# Write a function to check if the given two strings are anagrams or not. Return ‘Yes’ if they are anagrams, otherwise, return ‘No’.
# Example
# Input 1: build
# Input 2: dubli
# Output:
# Yes

#----------------------------------------------------------------------------------------------------------------
def check_anagrams(str_1,str_2):
  if str_1 > str_2: 
    for item in str_1:
      if item not in str_2:
        return 'No'
        
  else:
    for item in str_2:
      if item not in str_1:
        return 'No'
        
  return 'Yes'        

#input
str_1 = input()
str_2 = input()

ans = check_anagrams(str_1, str_2)
print(ans)



    
