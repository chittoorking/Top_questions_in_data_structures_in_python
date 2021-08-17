print("This is python progarm to check if a given string is palindrome or not")
def isPalindrome(s):
    return s==s[::-1]
s=input("Enter the string to check if a string is palindrome or not")
ans=isPalindrome(s)
if ans:
    print('Yes')
else:
    print("No")
    