print("This is python program to check if a string is palindrome or not")
string=input("Enter a string to check if it is palindrome or not")
l=len(string)
def isPalindrome(string):
    for i in range(0,int(len(string)/2)):
      if string[i]==string[l-i-1]:
        flag=0
        continue
      else :
         flag=1
    return flag
ans=isPalindrome(string)
if ans==0:
    print("Yes")
else:
    print("No")
 
    



       
