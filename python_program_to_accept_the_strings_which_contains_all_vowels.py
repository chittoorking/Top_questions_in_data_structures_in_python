print("This is python program to accept the strings if all vowels are present ")
s1=input("Enter a string")
flag=0
if not 'a' in s1:
        flag=1 
if not 'e' in s1:
        flag=1
if not 'i' in s1:
        flag=1
if not 'o' in s1:
        flag=1
if not 'u'  in s1:
        flag=1
if flag==0:
    print('accepted')
elif flag==1:
    print("Not accepted")
#Given a string, the task is check if every vowel is present or not. We consider a
#vowel to be present if it is present in upper case or lower case. i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’
#or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ .